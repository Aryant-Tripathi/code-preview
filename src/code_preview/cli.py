import argparse
import os
from rich.console import Console

from code_preview.git_utils import get_changed_files, get_file_diff
from code_preview.diff_renderer import render_diff

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Preview uncommitted code changes with syntax highlighting")
    parser.add_argument("path", nargs="?", default=".", help="Directory or file to preview (default: current directory)")
    args = parser.parse_args()

    repo_path = os.path.abspath(args.path)
    changed_files = get_changed_files(repo_path)

    if not changed_files:
        console.print("[green]No uncommitted changes found![/green]")
        return

    for file_path in changed_files:
        diff_text = get_file_diff(file_path)
        render_diff(file_path, diff_text)

if __name__ == "__main__":
    main()