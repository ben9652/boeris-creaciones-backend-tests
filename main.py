import unittest

if __name__ == '__main__':
    test_dir = './tests'
    test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_purchases.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)