from rich.syntax import Syntax
from rich.panel import Panel
from rich.console import Console

console = Console()

def render_diff(file_path, diff_text):
    if not diff_text:
        return

    syntax = Syntax("\n".join(diff_text), "diff", theme="monokai", line_numbers=False)
    console.print(
        Panel(
            syntax,
            title=f"[bold yellow]{file_path}",
            border_style="cyan"
        )
    )
