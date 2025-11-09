import os
from git import Repo
from difflib import unified_diff

def get_repo(path):
    try:
        return Repo(path, search_parent_directories=True)
    except:
        return None

def get_changed_files(path="."):
    repo = get_repo(path)
    if not repo:
        return []
    return [item.a_path for item in repo.index.diff(None)]

def get_file_diff(file_path):
    repo = get_repo(os.getcwd())
    if not repo or not repo.head.is_valid():
        old_content = []
    else:
        try:
            old_content = repo.git.show(f'HEAD:{file_path}').splitlines()
        except:
            old_content = []

    # ✅ Convert to absolute path based on repo root
    abs_path = os.path.join(repo.working_tree_dir, file_path)

    if not os.path.exists(abs_path):
        return []

    with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
        new_content = f.read().splitlines()

    return list(unified_diff(
        old_content,
        new_content,
        fromfile=f"a/{file_path}",
        tofile=f"b/{file_path}",
        lineterm=""
    ))
