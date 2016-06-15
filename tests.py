#!/usr/bin/env python

import unittest


class MyTest(unittest.TestCase):

	def test_one(self):
		self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()