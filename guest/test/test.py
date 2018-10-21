#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-09 23:35:13
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

import unittest

from module import Calculator

class ModuleTest(unittest.TestCase):
	def setUp(self):
		self.cal = Calculator(8, 4)

	def tearDown(self):
		pass

	def test_add(self):
		result = self.cal.add()
		self.assertEqual(result, 12)

	def test_sub(self):
		result = self.cal.sub()
		self.assertEqual(result, 4)

	def test_mul(self):
		result = self.cal.mul()
		self.assertEqual(result, 32)

	def test_div(self):
		result = self.cal.div()
		self.assertEqual(result, 2)

if __name__ == "__main__":
	unittest.main()
	# constrctor test collection
	suite = unittest.TestSuite()
	suite.addTest(ModuleTest("test_add"))
	suite.addTest(ModuleTest("test_sub"))
	suite.addTest(ModuleTest("test_mul"))
	suite.addTest(ModuleTest("test_div"))

	# execute testcase
	runner = unittest.TextTestRunner()
	runner.run(suite)
