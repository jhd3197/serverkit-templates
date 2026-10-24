"""Docker integration check: bootstrap credentials and persisted password rotation."""
import json
import secrets
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

import yaml

from compose_check import ROOT, render


def request(base, path, body, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(base + "/api/v1/auth/" + path,
                                 data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def main():
    template = yaml.safe_load((ROOT / "templates/solidping.yaml").read_text())
    name = "solidping-check-" + secrets.token_hex(4)
    text, values, files = render(template, name, [19370])
    base = "http://127.0.0.1:" + values["HTTP_PORT"]
    login = lambda password: request(base, "login", {
        "org": "default", "email": "admin@solidping.io", "password": password})
    with tempfile.TemporaryDirectory(prefix=name) as directory:
        root = Path(directory)
        (root / "compose.yaml").write_text(text)
        for filename, content in files:
            (root / filename).write_text(content)
        cmd = ["docker", "compose", "-p", name, "-f", str(root / "compose.yaml")]
        def compose(*args):
            subprocess.run(cmd + list(args), check=True, timeout=240,
                           stdout=subprocess.DEVNULL)
        try:
            compose("up", "-d")
            token = login(values["ADMIN_PASSWORD"])["accessToken"]
            try:
                login("solidpass")
                raise AssertionError("Public seed password still accepted")
            except urllib.error.HTTPError as error:
                assert error.code == 401
            bindings = subprocess.check_output(cmd + ["port", "web", "4000"], text=True)
            assert bindings.strip() == "127.0.0.1:" + values["HTTP_PORT"]
            changed = "Changed-" + secrets.token_hex(20)
            request(base, "change-password", {
                "currentPassword": values["ADMIN_PASSWORD"], "newPassword": changed}, token)
            compose("down")
            compose("up", "-d")
            assert login(changed)["accessToken"]
            try:
                login(values["ADMIN_PASSWORD"])
                raise AssertionError("Bootstrap reset the operator's password")
            except urllib.error.HTTPError as error:
                assert error.code == 401
            print("PASS: generated login, seed rejected, loopback binding, changed password survives recreation")
        finally:
            compose("down", "-v", "--remove-orphans")


if __name__ == "__main__":
    main()
