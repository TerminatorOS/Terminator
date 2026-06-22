import os, json, tarfile, requests
from pathlib import Path
from core.utils import compare_versions
from core.download import download_game, download

BASE = "/terminator/games"

def load_mirrors():
    try:
        with open("/etc/terminator/mirrors.conf") as f:
            return [x.strip() for x in f if x.strip()]
    except:
        return []

def is_installed(name):
    path = f"{BASE}/{name}/metadata.json"
    return os.path.exists(path)

def get_local_version(name):
    try:
        with open(f"{BASE}/{name}/metadata.json") as f:
            return json.load(f)["version"]
    except:
        return None

def install_game(name):
    mirrors = load_mirrors()

    for m in mirrors:
        base = f"{m.rstrip('/')}/{name}/"

        manifest = requests.get(base + "manifest.json").json()
        server_version = manifest["version"]

        if is_installed(name):
            local_version = get_local_version(name)

            cmp = compare_versions(server_version, local_version)

            if cmp == 0:
                print("Game already installed")
                return

            if cmp < 0:
                print("Local version is newer than server (wtf state)")
                return

            print("Update available, switching to update flow...")
            remove_game(name)

        print(f"[+] Installing {name} v{server_version}")

        tar_path = download_game(
            name=name,
            url=base + "game.tar.xz",
            version=manifest["version"]
        )
        # download(base + "game.tar.xz", tar_path)

        game_dir = f"{BASE}/{name}"
        os.makedirs(game_dir, exist_ok=True)

        with tarfile.open(tar_path, "r:xz") as tar:
            tar.extractall(game_dir)

        with open(f"{game_dir}/metadata.json", "w") as f:
            json.dump(manifest, f, indent=2)

        print("Installed successfully")
        return
