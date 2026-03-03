"""
Production code for the TDD lab.
Simple string-processing functions and a small command-line interface.
"""

from __future__ import annotations

import sys


def reverse_word(word: str) -> str:
    """
    Return the reverse of word.
    For example: hello -> olleh
    """
    return word[::-1]


def reverse_all_words(phrase: str) -> str:
    """
    Reverse each word in phrase while keeping word order.
    """
    return " ".join(reverse_word(w) for w in phrase.split())


def main() -> None:
    """
    Command-line entry point.
    """
    phrase = " ".join(sys.argv[1:])
    print(reverse_all_words(phrase))


if __name__ == "__main__":
    main()
