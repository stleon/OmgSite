#!/usr/bin/python3
# -*- coding: utf-8 -*-


class SiteException(Exception):
	def __str__(self):
		return 'Длина домена не должна превышать 255 символов!'