#!/usr/bin/python3
# -*- coding: utf-8 -*-


class SiteException(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message