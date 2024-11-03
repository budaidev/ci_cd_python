"""Test module for the character counter functionality."""
from pathlib import Path

import pytest

from character_counter.counter import count_characters


@pytest.fixture(scope="session")
def test_files(tmp_path_factory):
    """
    Create temporary test files for character counting tests.

    Returns:
        Dictionary containing paths to test files:
            - empty: An empty file
            - sample: A file with sample content
            - nonexistent: A path to a nonexistent file
    """
    base_dir = tmp_path_factory.mktemp("test_files")

    # Create empty file
    empty_file = base_dir / "empty.txt"
    empty_file.write_text("")

    # Create sample file
    sample_file = base_dir / "sample.txt"
    sample_file.write_text("Hello, World!")

    # Create non-existent file path
    nonexistent_file = base_dir / "nonexistent.txt"

    return {
        "empty": empty_file,
        "sample": sample_file,
        "nonexistent": nonexistent_file
    }


def test_empty_file(test_files):
    """Test counting characters in an empty file."""
    result = count_characters(test_files["empty"])
    assert result == 0


def test_sample_file(test_files):
    """Test counting characters in a file with content."""
    result = count_characters(test_files["sample"])
    assert result == 13  # "Hello, World!" has 13 characters


def test_nonexistent_file(test_files):
    """Test handling of non-existent file."""
    result = count_characters(test_files["nonexistent"])
    assert result is None


def test_invalid_path():
    """Test handling of invalid path."""
    result = count_characters(Path("/invalid/path/that/should/not/exist.txt"))
    assert result is None
