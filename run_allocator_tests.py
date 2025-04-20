import unittest
import sys

sys.path.insert(0, '.')

loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_allocator.py')

runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
runner.run(suite)
