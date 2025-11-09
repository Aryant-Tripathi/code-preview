# Code Preview

A universal CLI tool to preview **uncommitted code changes** with rich syntax highlighting — before you commit them.  
It works with **any language** and **any Git repository**.

Quickly visualize what your next commit will look like — right in your terminal.

-----

##  Features

  * **Colored Diff Preview**: Additions (green), deletions (red), and context (gray).
  * **Language-Agnostic**: Works for Java, Python, JavaScript, Scala, Go, etc.
  * **Rich Terminal Output**: Powered by [Textualize Rich](https://github.com/Textualize/rich).
  * **Git-Integrated**: Shows all unstaged and staged file changes.
  * **No Commit Required**: Safe to preview changes locally anytime.
  * **Extensible Design**: Add plugins or render to HTML in the future.

-----

## Example Output

Here is a preview of what changed in a Java file:

```diff
──────────────────────────────────────────────────────────────
a/src/main/java/com/example/App.java → b/src/main/java/com/example/App.java

@@ -14,6 +14,8 @@
 public class App {
     public static void main(String[] args) {
-        System.out.println("Hello, world!");
+        System.out.println("Hello, Aryant!");
+        System.out.println("Code preview is working");
     }
 }
──────────────────────────────────────────────────────────────
```

-----

## Installation

### From PyPI (Recommended)

You can install `code-preview` using `pip`:

```sh
pip install code-preview
```

### From Source

If you want to install it from your local folder for development:

```sh
git clone https://github.com/Aryant-Tripathi/code-preview.git
cd code-preview
pip install -e .
```

-----

##  Usage

### Preview All Unstaged Changes

Simply run the command in the root of your Git repository:

```sh
code-preview
```

### Preview Changes in a Specific Folder

You can limit the preview to a specific directory or file:

```sh
code-preview src/
```

### Run Directly Without Installation

You can also run the tool directly as a Python module:

```sh
python -m code_preview.cli
```

-----

## How It Works

1.  Detects all files with uncommitted changes using **GitPython**.
2.  Reads their last committed version (HEAD).
3.  Compares against your local version using **difflib**.
4.  Renders the diff with syntax highlighting via **Rich**.

-----

## Roadmap

  * [ ] Auto-detect syntax for each file type (`.java`, `.py`, `.js`, etc.)
  * [ ] Add `--html` mode for browser-based diff preview
  * [ ] Add `--watch` mode for real-time change tracking
  * [ ] Support for non-Git directories (via snapshots)
  * [ ] VSCode/IntelliJ plugin integration

-----

## Development

Interested in contributing? Here's how to set up your environment.

### Setup Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Install the project in "editable" mode:

```sh
pip install -e .
```

### Run Locally

Run the tool using the development entry point:

```sh
python -m code_preview.cli
```

### Project Structure

```text
code-preview/
├── src/
│   └── code_preview/
│       ├── __init__.py         # Package initializer
│       ├── cli.py              # Main CLI entry point (argparse)
│       ├── git_utils.py        # Git interaction logic
│       ├── diff_renderer.py    # Logic for rendering diffs with Rich
│       └── file_utils.py       # File reading utilities
├── pyproject.toml              # Build configuration (PEP 621)
├── setup.cfg                   # Package metadata
├── README.md
└── LICENSE
```

-----

## Publishing (For Maintainers)

1.  **Build**:

    ```sh
    python3 -m build
    ```

2.  **Upload to TestPyPI**:

    ```sh
    python3 -m twine upload --repository testpypi dist/*
    ```

3.  **Test Install**:

    ```sh
    pip install -i https://test.pypi.org/simple/ code-preview
    ```

4.  **Publish to PyPI**:

    ```sh
    python3 -m twine upload dist/*
    ```

-----

## Contributing

Contributions are welcome\! If you find this project useful:

  * **Star it on GitHub** → [Aryant-Tripathi/code-preview](https://www.google.com/search?q=https://github.com/Aryant-Tripathi/code-preview)
  * Open **issues** for feature requests or bugs
  * Submit **pull requests** for enhancements

-----

## Acknowledgements

  * [Rich](https://github.com/Textualize/rich) for beautiful terminal rendering
  * [GitPython](https://github.com/gitpython-developers/GitPython) for Git integration
  * Inspired by the need for more readable `git diff` previews for all developers

-----

##  Author

**Aryant Tripathi**

  * Software Engineer | Open Source Contributor | DSA Mentor
  * **Email**: aryanttripathi@gmail.com
  * **GitHub**: [@Aryant-Tripathi](https://github.com/Aryant-Tripathi)
  * **LinkedIn**: [in/aryant-tripathi](https://www.linkedin.com/in/aryanttripathi/)

-----

## License

This project is licensed under the Apache-2.0 License — see the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.