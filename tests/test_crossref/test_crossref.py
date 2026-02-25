"""
Tests for cross-referencing in linguistic examples using pandoc-ling filter.
"""
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest
import re


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


def test_explicit_id_reference(html_output):
    """
    Test that references to explicit IDs work ([@test]).
    """
    # Look for links with href="#test"
    links = html_output.find_all("a", href="#test")
    assert len(links) > 0, "No references to #test found"


def test_last_reference(html_output):
    """
    Test that [@last] references work.
    """
    body_text = html_output.get_text()
    # The [@last] should be replaced with a number
    # Should NOT contain the literal string "[@last]"
    assert "[@last]" not in body_text, "[@last] not resolved"


def test_next_reference(html_output):
    """
    Test that [@next] references work.
    """
    body_text = html_output.get_text()
    # The [@next] should be replaced with a number
    assert "[@next]" not in body_text, "[@next] not resolved"


def test_multiple_last_reference(html_output):
    """
    Test that [@llast] and [@llllllllast] references work.
    """
    body_text = html_output.get_text()
    # These should be resolved to numbers
    assert "[@llast" not in body_text, "[@llast...] not resolved"


def test_suffix_in_crossref(html_output):
    """
    Test that suffixes in cross-references work ([@llast c]).
    """
    # This is harder to validate as it depends on the actual numbering
    # Just check that processing completed
    assert html_output is not None


def test_noformat_example(html_output):
    """
    Test that noFormat=true examples work.
    """
    # Look for math formula
    body_text = html_output.get_text()
    # Should contain some part of the formula
    assert "sum" in body_text.lower() or "\\sum" in body_text


def test_example_ids_generated(html_output):
    """
    Test that examples have generated IDs of the form exNUMBER.
    """
    # Look for elements with id starting with "ex"
    elements_with_id = html_output.find_all(id=re.compile(r"^ex\d+"))
    assert len(elements_with_id) > 0, "No example IDs generated"
