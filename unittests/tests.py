#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class MyTestRunner(unittest.TextTestRunner):

	def __init__(self, *args, **kwargs):
		super(unittest.TextTestRunner, self).__init__()


class MyTest(unittest.TestCase):

	def test_one(self):
		self.assertTrue(True)

	def test_two(self):
		self.assertFalse(not True)


if __name__ == '__main__':
#	suite = unittest.TestSuite()
#	suite.addTest(unittest.makeSuite(MyTest))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(unittest.makeSuite(MyTest))
#	unittest.main()
