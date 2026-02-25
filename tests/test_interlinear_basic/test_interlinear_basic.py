"""
Test for basic interlinear examples.
"""
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest


@pytest.fixture(scope="module")
def html_output():
    """Generate HTML output for basic interlinear example."""
    test_dir = Path(__file__).parent
    input_md = test_dir / "input.md"
    output_html = test_dir / "output.html"
    filter_path = test_dir.parent.parent / "pandoc-ling.lua"

    subprocess.run(
        [
            "pandoc", str(input_md),
            "--lua-filter", str(filter_path),
            "-s",
            "-o", str(output_html)
        ],
        check=True
    )

    with open(output_html, "r", encoding="utf-8") as f:
        html_content = f.read()

    return BeautifulSoup(html_content, "html.parser")


def test_table_exists(html_output):
    """Test that interlinear example is converted to table."""
    tables = html_output.find_all("table", class_="linguistic-example")
    assert len(tables) > 0, "No linguistic example table found"


def test_dutch_text_present(html_output):
    """Test that the Dutch text is in the output."""
    body_text = html_output.get_text()
    assert "Deze zin is in het nederlands" in body_text or "Deze" in body_text
