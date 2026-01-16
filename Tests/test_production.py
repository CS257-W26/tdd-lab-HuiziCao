'''
A file for tests for the production code.
'''

from production import reverse_word
import sys
import unittest
from io import StringIO
import production

class TestReverseWord(unittest.TestCase):
  
  def test_reverse_normal_word(self):
    self.assertEqual(production.reverse_word("hello"), "olleh")
  
  def test_reverse_single_char(self):
    self.assertEqual(production.reverse_word("a"), "a")
  
  def test_reverse_empty_string(self):
    self.assertEqual(production.reverse_word(""), "")
  

class TestReverseAllWords(unittest.TestCase):
  def test_example_phrase(self):
    self.assertEqual(production.reverse_all_words("this is a test"), "siht si a tset")
  
  def test_one_word_phrase(self):
    self.assertEqual(production.reverse_all_words("hello"), "olleh")

  def test_empty_phrase(self):
    self.assertEqual(production.reverse_all_words(""), "")

