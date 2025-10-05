import unittest
from utils import clean_text, word_count

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        raw = "  Hello\nWorld!  "
        expected = "hello world!"
        self.assertEqual(clean_text(raw), expected)

    def test_word_count(self):
        text = "hello world this is a test"
        self.assertEqual(word_count(text), 6)

if __name__ == "__main__":
    unittest.main()
