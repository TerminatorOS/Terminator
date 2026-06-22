import os, shutil
import requests
from core.installer import load_mirrors, is_installed, get_local_version
from core.utils import compare_versions

BASE = "/terminator/games"

def list_games():
    if not os.path.exists(BASE):
        print("No games installed")
        return

    for g in os.listdir(BASE):
        print("-", g)

def remove_game(name):
    path = f"{BASE}/{name}"
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Removed", name)

def update_game(name):
    mirrors = load_mirrors()

    for m in mirrors:
        base = f"{m.rstrip('/')}/{name}/"

        manifest = requests.get(base + "manifest.json").json()
        server_version = manifest["version"]

        if not is_installed(name):
            print("Not installed, installing instead...")
            install_game(name)
            return

        local_version = get_local_version(name)

        cmp = compare_versions(server_version, local_version)

        if cmp <= 0:
            print("Already up to date")
            return

        print("Updating game...")

        remove_game(name)
        install_game(name)
        return
