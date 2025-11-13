import os

IGNORE_PATTERNS = {
    "node_modules",
    "dist",
    "build",
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "temp",
    "tmp",
    ".DS_Store"
}

IGNORE_EXTS = {
    ".class",
    ".jar",
    ".zip",
    ".log",
    ".git",
}

def is_binary(path: str) -> bool:
    try:
        with open(str(path), "rb") as f:
            chunk = f.read(8000)
        return b"\0" in chunk
    except Exception:
        return False

def should_ignore(path: str) -> bool:
    parts = path.split(os.sep)

    # dir-based ignore
    if any(p in IGNORE_PATTERNS for p in parts):
        return True

    # extension-based ignore
    _, ext = os.path.splitext(path)
    if ext in IGNORE_EXTS:
        return True

    return False
