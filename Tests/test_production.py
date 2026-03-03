"""
Tests for production.py.
"""

from __future__ import annotations

import runpy
import sys
import unittest
from io import StringIO

import production


class TestReverseWord(unittest.TestCase):
    def test_reverse_normal_word(self) -> None:
        self.assertEqual(production.reverse_word("hello"), "olleh")

    def test_reverse_single_char(self) -> None:
        self.assertEqual(production.reverse_word("a"), "a")

    def test_reverse_empty_string(self) -> None:
        self.assertEqual(production.reverse_word(""), "")


class TestReverseAllWords(unittest.TestCase):
    def test_example_phrase(self) -> None:
        self.assertEqual(
            production.reverse_all_words("this is a test"), "siht si a tset"
        )

    def test_one_word_phrase(self) -> None:
        self.assertEqual(production.reverse_all_words("hello"), "olleh")

    def test_empty_phrase(self) -> None:
        self.assertEqual(production.reverse_all_words(""), "")


class TestMain(unittest.TestCase):
    def test_main_prints_transformed_phrase_single_arg(self) -> None:
        old_argv = sys.argv
        old_stdout = sys.stdout

        try:
            sys.argv = ["production.py", "this is a test"]
            sys.stdout = StringIO()

            production.main()

            printed_output = sys.stdout.getvalue()
            self.assertEqual(printed_output, "siht si a tset\n")
        finally:
            sys.argv = old_argv
            sys.stdout = old_stdout

    def test_main_prints_transformed_phrase_multi_arg(self) -> None:
        old_argv = sys.argv
        old_stdout = sys.stdout

        try:
            sys.argv = ["production.py", "this", "is", "a", "test"]
            sys.stdout = StringIO()

            production.main()

            printed_output = sys.stdout.getvalue()
            self.assertEqual(printed_output, "siht si a tset\n")
        finally:
            sys.argv = old_argv
            sys.stdout = old_stdout

    def test_main_with_no_phrase_prints_blank_line(self) -> None:
        old_argv = sys.argv
        old_stdout = sys.stdout

        try:
            sys.argv = ["production.py"]
            sys.stdout = StringIO()

            production.main()

            printed_output = sys.stdout.getvalue()
            self.assertEqual(printed_output, "\n")
        finally:
            sys.argv = old_argv
            sys.stdout = old_stdout


class TestScriptEntrypoint(unittest.TestCase):
    def test_running_module_as_main_calls_main(self) -> None:
        old_argv = sys.argv
        old_stdout = sys.stdout

        try:
            sys.argv = ["production.py", "this is a test"]
            sys.stdout = StringIO()

            runpy.run_module("production", run_name="__main__")

            printed_output = sys.stdout.getvalue()
            self.assertEqual(printed_output, "siht si a tset\n")
        finally:
            sys.argv = old_argv
            sys.stdout = old_stdout
