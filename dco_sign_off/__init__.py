#!/usr/bin/env python3
"""Adds a DCO Signed-off-by line to commit messages if not already present."""

import subprocess
import sys


def main():
    commit_msg_file = sys.argv[1]

    with open(commit_msg_file, "r") as f:
        contents = f.read()

    if "Signed-off-by: " in contents:
        return

    ident = subprocess.check_output(["git", "var", "GIT_COMMITTER_IDENT"], text=True).strip()
    # ident format: "Name <email> timestamp tz" — keep "Name <email>"
    sob = "Signed-off-by: " + ident.rsplit(" ", 2)[0]

    with open(commit_msg_file, "a") as f:
        f.write(f"\n{sob}\n")


if __name__ == "__main__":
    main()
