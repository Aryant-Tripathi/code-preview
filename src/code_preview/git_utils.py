import os
from git import Repo
from difflib import unified_diff

def get_repo(path = "."):
    try:
        return Repo(path, search_parent_directories=True)
    except:
        return None

def get_tracked_changes(path="."):
    """
    Default mode:
    Return ONLY tracked file changes (staged + unstaged)
    """
    repo = get_repo(path)
    if not repo:
        return []

    changed = set()

    # staged changes
    for diff in repo.index.diff("HEAD"):
        changed.add(diff.a_path)

    # unstaged tracked changes
    for diff in repo.index.diff(None):
        # Only include if file exists in HEAD (tracked)
        try:
            repo.git.show(f"HEAD:{diff.a_path}")
            changed.add(diff.a_path)
        except:
            pass  # skip untracked files

    return sorted(changed)

def get_all_changes_grouped(path="."):
    """
    Returns 3 categories:
       - staged
       - unstaged
       - untracked
    """
    repo = get_repo(path)
    if not repo:
        return [], [], []

    staged = set()
    unstaged = set()
    untracked = set()

    for diff in repo.index.diff("HEAD"):
        staged.add(diff.a_path)

    for diff in repo.index.diff(None):
        unstaged.add(diff.a_path)

    for f in repo.untracked_files:
        untracked.add(f)

    return sorted(staged), sorted(unstaged), sorted(untracked)

def get_file_diff(file_path):

    repo = get_repo(os.getcwd())
    if not repo:
        return []

    try:
        old_content = repo.git.show(f'HEAD:{file_path}').splitlines()
    except Exception as e:
        old_content = [] #If the file is new (not in HEAD), this raises; we treat “old” as empty.

    abs_path = os.path.join(repo.working_tree_dir, file_path)

    if not os.path.exists(abs_path):
        new_content = []
    else:
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            new_content = f.read().splitlines()

    return list(
        unified_diff(
            old_content,
            new_content,
            fromfile=f"a/{file_path}",
            tofile=f"b/{file_path}",
            lineterm=""
        )
    )
