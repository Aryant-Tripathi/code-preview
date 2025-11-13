import argparse
import os

import requests
from rich.console import Console

from code_preview.git_utils import (
    get_file_diff,
    get_tracked_changes, get_all_changes_grouped
)
from code_preview.diff_renderer import render_diff
from code_preview.file_utils import should_ignore, is_binary
from code_preview import __version__
from packaging import version

console = Console()

def main():
    parser = argparse.ArgumentParser(
        description="Preview uncommitted (and staged) code changes with syntax highlighting"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Show both staged and unstaged changes (including new files)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"code-preview {__version__}"
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to repository or directory (default: current directory)"
    )

    args = parser.parse_args()
    repo_path = os.path.abspath(args.path)

    if not args.all:
        changed_files = get_tracked_changes(repo_path)

        if not changed_files:
            console.print("[green]No tracked changes found![/green]")
            return

        for file_path in changed_files:
            if should_ignore(file_path):
                continue

            abs_path = os.path.join(repo_path, str(file_path))
            if is_binary(abs_path):
                console.print(f"[yellow]Skipping binary file:[/yellow] {file_path}")
                continue

            diff_lines = get_file_diff(file_path)
            render_diff(file_path, diff_lines)
        return

    staged, unstaged, untracked = get_all_changes_grouped(repo_path)

    if not (staged or unstaged or untracked):
        console.print("[green]No changes found![/green]")
        return


    if staged:
        console.rule("[green] STAGED CHANGES")
        for file_path in staged:

            if should_ignore(file_path):
                continue

            abs_path = os.path.join(repo_path, str(file_path))
            if is_binary(abs_path):
                console.print(f"[yellow]Skipping binary file:[/yellow] {file_path}")
                continue

            diff_lines = get_file_diff(file_path)
            render_diff(file_path, diff_lines)

    if unstaged:
        console.rule("[yellow] UNSTAGED CHANGES")
        for file_path in unstaged:

            if should_ignore(file_path):
                continue

            abs_path = os.path.join(repo_path, str(file_path))
            if is_binary(abs_path):
                console.print(f"[yellow]Skipping binary file:[/yellow] {file_path}")
                continue

            diff_lines = get_file_diff(file_path)
            render_diff(file_path, diff_lines)

    if untracked:
        console.rule("[cyan] NEW FILES (UNTRACKED)")
        for file_path in untracked:

            if should_ignore(file_path):
                continue

            abs_path = os.path.join(repo_path, str(file_path))
            if is_binary(abs_path):
                console.print(f"[yellow]Skipping binary file:[/yellow] {file_path}")
                continue

            diff_lines = get_file_diff(file_path)
            render_diff(file_path, diff_lines)

    check_for_update()

def check_for_update():
    try:
        response = requests.get("https://pypi.org/pypi/code-preview/json", timeout=1)
        if response.status_code != 200:
            return

        data = response.json()
        latest_version = data["info"]["version"]

        if version.parse(latest_version) > version.parse(__version__):
            console.print(
                f"[bold cyan][notice][/bold cyan] A new release of code-preview is available: "
                f"{__version__} → {latest_version}"
            )
            console.print(
                "[bold cyan][notice][/bold cyan] To update, run: "
                "pip install --upgrade code-preview"
            )

    except Exception:
        pass

if __name__ == "__main__":
    main()