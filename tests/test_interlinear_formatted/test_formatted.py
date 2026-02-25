"""
Test for formatted interlinear examples with formatGloss=true.
"""
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest


@pytest.fixture(scope="module")
def html_output():
    """Generate HTML output for formatted interlinear example."""
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
    """Test that formatted interlinear example is converted to table."""
    tables = html_output.find_all("table", class_="linguistic-example")
    assert len(tables) > 0, "No linguistic example table found"


def test_formatting_applied(html_output):
    """Test that formatGloss=true applies formatting."""
    em_tags = html_output.find_all("em")
    span_smallcaps = html_output.find_all("span", class_="smallcaps")
    
    assert len(em_tags) > 0 or len(span_smallcaps) > 0, \
        "No formatting applied with formatGloss=true"
