#!/usr/bin/python3
# -*- coding: utf-8 -*-
import microdata
import requests


class MicroFormat():
	def __init__(self, path):
		try:
			self.data = microdata.get_items(requests.get(path).text)[0].json()
			self.error = None
		except IndexError:
			self.error = 'NOTHING FOUND'
		except requests.exceptions.ConnectionError:
			self.error = 'NO HOST AVAILABLE'
	def __str__(self):
		if self.error:
			return str(self.error)
		else:
			return self.data

if __name__ == '__main__':
	print(MicroFormat(input('Enter path, please: ')))