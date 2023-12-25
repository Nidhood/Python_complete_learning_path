import unittest
import test_cap # import the cap.py file

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Python') # assertEqual() method

    def test_multiple_words(self):
        text = 'monty python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Monty Python') # assertEqual() method

if __name__ == '__main__':
    unittest.main() # run the test_cap.py file