import os
import subprocess

BASE = "/terminator/games"

def launch_game(name):
    game_dir = f"{BASE}/{name}"
    entry = f"{game_dir}/launch.sh"

    if not os.path.exists(entry):
        print("Game not installed or missing launch.sh")
        return

    os.chmod(entry, 0o755)
    subprocess.run(["bash", entry], cwd=game_dir)
