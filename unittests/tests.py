#!/usr/bin/env python

import warnings

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class MyTestRunner(unittest.TextTestRunner):

	def __init__(self, *args, **kwargs):
		super(unittest.TextTestRunner, self).__init__()


class MyTest(unittest.TestCase):

	def test_one(self):
		warnings.warn("i am fake warning")
		self.assertTrue(True)

	def test_two(self):
		self.assertFalse(not True)

	def test_three(self):
		self.assertFalse(not True)

#	def test_err(self):
#		self.assertEquals(1, 0)

	def test_skip(self):
		raise unittest.SkipTest

class AnotherTestCase(unittest.TestCase):

	def test_another_one(self):
		self.assertTrue(True)

	def test_second(self):
		self.assertEquals(1, 1)

	def test_3(self):
		self.assertTrue(True)

	def test_fail(self)
		1/0

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(MyTest))
	suite.addTest(unittest.makeSuite(AnotherTestCase))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
