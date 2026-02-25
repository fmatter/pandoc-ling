"""
Test interlinear with simple judgement (^*).
"""
import subprocess
from pathlib import Path
import pytest


def test_simple_judgement():
    """Test that simple judgement ^* works in interlinear."""
    test_dir = Path(__file__).parent
    input_md = test_dir / "input.md"
    output_html = test_dir / "output.html"
    filter_path = test_dir.parent.parent / "pandoc-ling.lua"

    result = subprocess.run(
        [
            "pandoc", str(input_md),
            "--lua-filter", str(filter_path),
            "-s",
            "-o", str(output_html)
        ],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Pandoc failed: {result.stderr}"
