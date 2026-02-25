"""
Test for complex example mixing labels, interlinear, and single-line examples.
"""
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest


@pytest.fixture(scope="module")
def html_output():
    """Generate HTML output for complex mixed example."""
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
    """Test that complex example is converted to table."""
    tables = html_output.find_all("table", class_="linguistic-example")
    assert len(tables) > 0, "No linguistic example table found"


def test_preamble_present(html_output):
    """Test that preamble is in the output."""
    body_text = html_output.get_text()
    assert "Completely superfluous preamble" in body_text


def test_mixed_content(html_output):
    """Test that both interlinear and single-line examples work together."""
    body_text = html_output.get_text()
    assert "Mixing single line examples" in body_text
