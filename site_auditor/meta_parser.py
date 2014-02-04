# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser


class MetaHTMLParser(HTMLParser):
	""" Gets meta description and meta keywords """
	def __init__(self):
		HTMLParser.__init__(self)
		self.meta = {'description': 'NO', 'keywords': 'NO'}

	def handle_starttag(self, tag, attrs):
		"""
		Checks, if meta tags are well written. If true - save it in self.meta
		"""
		if tag.lower() == 'meta':
			#print attrs
			if len(attrs[0]) == 2 and len(attrs[0]) == 2 and attrs[0][1].lower() in self.meta.keys() \
				and attrs[1][0].lower() == 'content':
				self.meta[attrs[0][1].lower()] = attrs[1][1]

if __name__ == '__main__':
	p = MetaHTMLParser()
	p.feed('<html><head><title>Test</title><meta name="description" content="123123"><meta '
								'name="keywords" content="11111"></head>''<body><h1>Parse me!</h1></body></html>')
	print p.meta
	p.close()