"""Fail if a live API token is committed in source or notebook output."""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints"}

# Flag api_token query values that are literals. Placeholders such as
# {token} and shell-style $TOKEN are allowed.
LITERAL_API_TOKEN = re.compile(
    r"api_token=(?!\{)(?!\$)[A-Za-z0-9][A-Za-z0-9._-]{6,}"
)


def _text_files():
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if SKIP_DIRS.intersection(path.relative_to(REPO_ROOT).parts):
            continue
        yield path


def test_no_hardcoded_api_tokens():
    offenders = []
    for path in _text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if LITERAL_API_TOKEN.search(text):
            offenders.append(str(path.relative_to(REPO_ROOT)))
    assert offenders == []


def test_dataloader_reads_eodhd_token_from_environment():
    path = REPO_ROOT / "src" / "dataExploration" / "dataloader.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    sources = "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook["cells"]
        if cell.get("cell_type") == "code"
    )
    assert sources.count('os.environ["EODHD_API_TOKEN"]') == 2
    assert sources.count("api_token={token}") == 7
    assert LITERAL_API_TOKEN.search(path.read_text(encoding="utf-8")) is None
