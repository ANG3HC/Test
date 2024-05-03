import unittest
from a import func

class TestFunc(unittest.TestCase):
    def test_func(self):
        # Test the output of the func function
        expected_output = 'test'
        with captured_output() as (out, err):
            func()
        self.assertEqual(out.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()