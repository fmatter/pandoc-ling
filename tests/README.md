# pandoc-ling Test Battery

This test battery validates the functionality of the pandoc-ling filter using the exact examples from the readme.md.

## Test Structure

## Test Results: 23 passed ✅

**All Tests Passing:**
- **test_basic/**: Basic linguistic examples (numbering, labels, judgements, preambles) - 5 tests
- **test_crossref/**: Cross-referencing features ([@test], [@last], [@next]) - 7 tests
- **test_interlinear_basic/**: Basic 4-line interlinear examples - 2 tests
- **test_interlinear_formatted/**: Formatted interlinear with formatGloss=true - 2 tests
- **test_interlinear_multiline/**: Multiline headers with \\\\ - 2 tests
- **test_interlinear_complex/**: Mixed labeled examples (interlinear + single-line) - 3 tests
- **test_interlinear_judgement_simple/**: Simple judgements (^*) in interlinear - 1 test
- **test_interlinear_judgement_question/**: Question judgements (^?) in interlinear - 1 test

**Note on Grammaticality Judgements:**
Simple judgements like `^*`, `^?`, and `^???` work correctly. Complex judgements with double carets and special characters (e.g., `^^:–)^`) are not supported by the filter.

## Running Tests

From the pandoc-ling directory:

```bash
pytest tests/
```

Or run specific test suites:

```bash
pytest tests/test_basic/                    # Basic examples
pytest tests/test_crossref/                 # Cross-references
pytest tests/test_interlinear_basic/        # Basic interlinear
pytest tests/test_interlinear_formatted/    # Formatted interlinear
pytest tests/test_interlinear_multiline/    # Multiline headers
pytest tests/test_interlinear_complex/      # Complex mixed examples
pytest tests/test_interlinear_judgement_*/  # Judgement tests
```

## Requirements

- pytest
- beautifulsoup4
- pandoc (installed and in PATH)

Install Python requirements:

```bash
pip install pytest beautifulsoup4
```

## Test Output

Each test generates an `output.html` file in its directory. These files can be inspected manually to verify the output looks correct.
