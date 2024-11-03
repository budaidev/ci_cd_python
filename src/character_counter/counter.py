"""Provide functionality for counting characters in text files."""
import sys
from pathlib import Path
from typing import Optional


def count_characters(file_path: Path) -> Optional[int]:
    """
    Count the number of characters in a text file.

    Args:
        file_path: Path to the text file

    Returns:
        Number of characters in the file, or None if file cannot be read
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main() -> None:
    """Run the character counter."""
    if len(sys.argv) != 2:
        print("Usage: python counter.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    result = count_characters(file_path)

    if result is not None:
        print(f"Number of characters: {result}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
