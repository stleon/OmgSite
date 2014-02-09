#!/usr/bin/python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser


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
	print(p.meta)
	p.close()

"""
html = '<html><head><title>Test</title><meta name="description" content="123123"><meta ' \
								'name="keywords" content="11111"></head>''<body><h1>Parse me!</h1></body></html>'

class MetaHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.meta = {'description': 'NO', 'keywords': 'NO'}

	def handle_starttag(self, tag, attrs):
		if tag.lower() == 'meta':

			if len(attrs[0]) == 2 and len(attrs[0]) == 2 and attrs[0][1].lower() in self.meta.keys() \
				and attrs[1][0].lower() == 'content':
				self.meta[attrs[0][1].lower()] = attrs[1][1]


def test1(html):
	p = MetaHTMLParser()
	p.feed(html)
	print(p.meta['description'])
	print(p.meta['keywords'])
	p.close()

# %timeit -n 1000 test1(html)
# 1000 loops, best of 3: 316 µs per loop
# %timeit -n 10000 test1(html)
# 10000 loops, best of 3: 313 µs per loop

def find_meta_tags_content(html, meta_tag):
		meta_tag_content = 'NO'
		match_meta_tag_str = re.compile(r'<meta[.\s\S]+?>', re.I)
		meta_tag_raws = re.findall(match_meta_tag_str, html)
		for raw in meta_tag_raws:
			if meta_tag in raw.lower():
				content_match = re.compile(r'content=(?:\'|\")([\s\S.]+)(?:\'|\")', re.I)
				if re.search(content_match, raw):
					meta_tag_content = re.search(content_match, raw).group(1)
		return meta_tag_content

def test2(html):
	print(find_meta_tags_content(html, 'description'))
	print(find_meta_tags_content(html, 'keywords'))
# %timeit -n 1000 test2(html)
# 1000 loops, best of 3: 101 µs per loop
# %timeit -n 10000 test2(html)
# 10000 loops, best of 3: 103 µs per loop
"""