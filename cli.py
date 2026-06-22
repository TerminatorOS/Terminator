#!/usr/bin/env python3

import sys
from core.installer import install_game
from core.launcher import launch_game
from core.registry import list_games, remove_game, update_game

def main():
    if len(sys.argv) < 2:
        print("Usage: terminator <install|launch|remove|update|list> ...")
        return

    cmd = sys.argv[1]

    if cmd == "install":
        install_game(sys.argv[2])
    elif cmd == "launch":
        launch_game(sys.argv[2])
    elif cmd == "remove":
        remove_game(sys.argv[2])
    elif cmd == "update":
        update_game(sys.argv[2])
    elif cmd == "list":
        list_games()
    elif cmd == "ver":
        print("Terminator Package Manager. Version 0.1")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
