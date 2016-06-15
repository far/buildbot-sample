#!/usr/bin/env python

import unittest


class MyTest(unittest.TestCase):

	def test_one(self):
		self.assertTrue(True)

	def test_two(self):
		self.assertFalse(not True)


if __name__ == '__main__':
    unittest.main()