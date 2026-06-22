from packaging import version

def make_filename(name, version):
    return f"{name}@{version}.tar.xz"

def compare_versions(v1, v2):
    """
    return:
      1 -> v1 > v2
      0 -> equal
     -1 -> v1 < v2
    """
    if version.parse(v1) > version.parse(v2):
        return 1
    elif version.parse(v1) < version.parse(v2):
        return -1
    return 0
