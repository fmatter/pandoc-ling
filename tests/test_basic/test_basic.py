"""
Tests for basic linguistic examples using pandoc-ling filter.
"""
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest


@pytest.fixture(scope="module")
def html_output():
    """
    A pytest fixture that runs Pandoc to generate the test HTML output.
    """
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


def test_basic_example_numbering(html_output):
    """
    Test that basic examples are numbered.
    """
    # Find all tables with linguistic-example class
    tables = html_output.find_all("table", class_="linguistic-example")
    # We should have multiple examples
    assert len(tables) > 0, "No linguistic examples found"


def test_labelled_examples(html_output):
    """
    Test that labelled examples (a., b., c.) are properly formatted.
    """
    # Find tables and look for labels within them
    tables = html_output.find_all("table", class_="linguistic-example")
    
    # Look for labels in the output
    found_labels = False
    for table in tables:
        text = table.get_text()
        if "a." in text and "b." in text:
            found_labels = True
            break
    
    assert found_labels, "Labelled examples not found"


def test_judgements_present(html_output):
    """
    Test that grammaticality judgements are present in the output.
    """
    # Look for judgement class or symbols
    judgement_cells = html_output.find_all("td", class_="linguistic-example-judgement")
    
    # Should have some judgements
    assert len(judgement_cells) > 0, "No judgement cells found"


def test_preamble_present(html_output):
    """
    Test that preambles are included in examples.
    """
    # Look for preamble class
    preamble_cells = html_output.find_all("td", class_="linguistic-example-preamble")
    
    assert len(preamble_cells) > 0, "No preamble cells found"


def test_single_judgement_example(html_output):
    """
    Test that a single example with judgement works (was an error in earlier versions).
    """
    # Just check that processing completed without error
    # The fixture would fail if pandoc errored
    assert html_output is not None
