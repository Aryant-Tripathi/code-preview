import os

TEXT_EXTS = {".py", ".java", ".js", ".ts", ".md", ".yml", ".yaml", ".json", ".txt"}

def is_binary(path: str) -> bool:
    try:
        with open(path, "rb") as f:
            chunk = f.read(8000)
        return b"\0" in chunk
    except Exception:
        return False

def should_ignore(path: str) -> bool:
    # add patterns as needed
    parts = path.split(os.sep)
    return any(p in {"node_modules", "dist", "build", ".git"} for p in parts)