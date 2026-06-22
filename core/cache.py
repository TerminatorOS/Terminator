import os
from core.dirs import DOWNLOAD_DIR

def get_cached_file(name, version):
    return f"{DOWNLOAD_DIR}/{name}@{version}.tar.xz"


def clear_old_versions(name):
    for f in os.listdir(DOWNLOAD_DIR):
        if f.startswith(name + "@"):
            os.remove(os.path.join(DOWNLOAD_DIR, f))
