import os
import subprocess
from core.cache import get_cached_file, clear_old_versions
from core.dirs import DOWNLOAD_DIR

def ensure_dir():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download(url, name):
    ensure_dir()

    path = f"{DOWNLOAD_DIR}/{name}"

    cmd = [
        "curl",
        "-L",
        "-C", "-", 
        "-o", path,
        "--progress-bar",
        "--no-verbose",
        url
    ]

    print(f"[↓] Downloading {name}")
    subprocess.run(cmd)

    return path

def download_game(name, url, version):
    ensure_dir()

    final_file = get_cached_file(name, version)

    if os.path.exists(final_file):
        print("[✓] Using cached version")
        return final_file

    clear_old_versions(name)

    print("[↓] Fetching new version...")

    tmp_file = download(url, f"{name}.tar.xz")

    os.rename(tmp_file, final_file)

    return final_file
