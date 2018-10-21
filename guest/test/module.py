#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 10:13:38
# @Author  : Kai Li (447252251@qq.com)
# @Link    : https://mail.qq.com/
# @Version : $Id$

class Calculator():
	"realize the addition、subtraction、multiplication、and division of two numbers"
	def __init__(self, a, b):
		self.a = int(a)
		self.b = int(b)

	# addition
	def add(self):
		return self.a + self.b

	# substraction
	def sub(self):
		return self.a - self.b

	# multiplication
	def mul(self):
		return self.a * self.b

	# division
	def div(self):
		return self.a / self.b
