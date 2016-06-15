#!/usr/bin/env python

import unittest2 as unittest

class MyTestRunner(unittest.TextTestRunner):

	def __init__(self, *args, **kwargs):
		super(TextTestRunner, self).__init__(*args, **kwargs)


class MyTest(unittest.TestCase):

	def test_one(self):
		self.assertTrue(True)

	def test_two(self):
		self.assertFalse(not True)


if __name__ == '__main__':
#	suite = unittest.TestSuite()
#	suite.addTest(unittest.makeSuite(MyTest))
	runner = MyTestRunner(verbosity=2)
	runner.run(unittest.makeSuite(MyTest))
#	unittest.main()