#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
from xml.dom.minidom import parseString
import random
import requests
from oexceptions import SiteException
import re
import time


class SiteAuditor():
	def __init__(self, site):
		try:
			self.start_time = time.time()
			self.site = self.clear_site_name(site)
			self.headers = self.my_headers()
			self.ip = socket.gethostbyname(self.site)
			self.request = requests.get('http://%s' % self.site, headers=self.headers)
			with open(r'out.txt') as output:
				self.output = output.read()
		except (socket.gaierror, requests.exceptions.ConnectionError):
			self.error = 'NO HOST AVAILABLE'
		except SiteException as error:
			self.error = error
		except FileNotFoundError:
			self.error = 'Не найден файл output.txt!'
		else:
			self.error = None
			self.whois = self.who()
			self.web_server = self.inf_from_headers('server')
			self.powered_by = self.inf_from_headers('x-powered-by')
			self.content_lanuage = self.inf_from_headers('content-language')
			self.content_type = self.inf_from_headers('content-type')
			self.html = self.request.text
			self.description = self.find_meta_tags_content('description')
			self.key_words = self.find_meta_tags_content('keywords')
			self.title = self.site_title()
			self.ya_metrica = self.analytics('yaCounter')
			self.google_an = self.analytics('google-analytics.com/ga.js')
			self.live_inet = self.analytics('counter.yadro.ru/hit')
			self.rambler_top = self.analytics('counter.rambler.ru/top100.jcn?')
			self.mail_rating = self.analytics('top.list.ru/counter?id=')
			self.yad = self.yandex()
			self.pr = self.page_rank()
			self.dmoz = self.dmoz_rank()
			self.alexa = self.alexa_rank()
			self.robots_txt = self.robots('robots.txt')
			self.sitemap_xml = self.robots('sitemap.xml')
			self.pro_index = self.index()
			self.mail_catalog = self.catalogs('Не найдено', 'http://search.list.mail.ru/?q=')
			self.yahoo_catalog = self.catalogs('We did not find', 'http://dir.search.yahoo.com/search?ei=UTF-8&h=c&p=')
			self.tdp_catalog = self.catalogs('No listings have been found', 'http://www.trustdirectory.org/search.php?what=')
			self.joomla = self.engine('administrator')
			self.word_press = self.engine('wp-login.php')
			self.umi = self.engine('admin/content/sitetree')
			self.ucoz = self.engine('panel')
			self.bitrix = self.engine('bitrix/admin')
			self.simple_login = self.engine('login')
			self.admin_login = self.engine('admin')
			self.modx = self.engine('manager')
			self.dle = self.engine('admin.php')
			self.drupal = self.engine('user')
			self.html_validator = self.html_valid()
			self.safe_site = self.safebrowsing()
			self.bing = list(map(self.bing_information, ['linkfromdomain:', 'site:']))
		finally:
			self.all_time = "%.2f seconds" % (time.time() - self.start_time)

	@staticmethod
	def clear_site_name(site):

		def check_symbols(i):
			if i not in '`~!№@"$;%^?&*()+{[]}|\\:<>,\' ':
				return i
			else:
				raise SiteException('Недопустимые символы в домене!')
		# регулярное выражение для поиска чистого домена
		clean_url = re.compile(r'(?:http[s]?)?:?(?:)?(?:/){0,2}([\w-]*.[\w-]*)')
		if re.search(clean_url, site).group(1):
			site = re.search(clean_url, site).group(1)
		site = site.strip()
		if len(site) > 255 or len(site) < 4:
			raise SiteException('Длина домена не должна превышать 255 символов или быть меньше 4!')
		if re.search(r'[а-яА-Я]', site):
			site = site.encode('idna').decode('utf-8')
		return ''.join(list(map(check_symbols, site)))

	def my_headers(self):
		useragents = [
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 \ '
			'(.NET CLR 3.5.30729)',
			'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 \ '
			'(.NET CLR 3.5.30729)',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1',
			'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) \ '
			'Chrome/4.0.219.6 Safari/532.1',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; \ '
			'.NET CLR 2.0.50727; InfoPath.2)',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; \ '
			'.NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
			'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
			'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
			'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51',
			# new
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \ '
			'Chrome/32.0.1700.102 Safari/537.36',
			'Mozilla/5.0 (Linux; Android 4.2.2; ru-ru; SAMSUNG GT-19500 Build/JDQ39) AppleWebKit/535.19 \ '
			'(KHTML, like Gecko) Version/1.0 Chrome/18.0.1025.308 Mobile Safari/535.19',

		]
		refers = [
			'https://www.google.com/?q=',
			'https://www.google.ru/?q=',
			'http://yandex.ru/yandsearch?text=',
			'http://go.mail.ru/search?&q=',
			'http://nova.rambler.ru/search?query='
		]
		return {
			'User-Agent': random.choice(useragents),
			'Cache-Control': random.choice(['no-cache', 'cache']),
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
			'Referer': '%s%s' % (random.choice(refers), self.site),
			'Keep-Alive': random.randint(110, 120),
			'Connection': 'keep-alive',
		}

	def inf_from_headers(self, string):
		try:
			return self.request.headers[string]
		except KeyError:
			return 'NO'

	def site_title(self):
		try:
			return self.html.split('<title>')[1].split('</title>')[0].strip()
		except IndexError:
			return 'NO'

	def analytics(self, string):
		return 'YES' if string in self.html else 'NO'

	def yandex(self):
		r = requests.get('http://bar-navig.yandex.ru/u?ver=2&url=http://%s&show=1' % self.site)
		xmldoc = parseString(r.text.encode('windows-1251'))
		tyc = xmldoc.getElementsByTagName('tcy')[0].attributes['value'].value
		if tyc == '-1':
			tyc = 0
		# TODO Yandex needs capcha
		r = requests.get('http://blogs.yandex.ru/search.xml?link=%s&noreask=1' % self.site, headers=self.headers).text
		try:
			blog_links = r.split(' из <b>')[1].split('</b> найденных.')[0].strip()
		except IndexError:
			blog_links = 'NEED CAPTCHA'
		#r = requests.get('http://yandex.ru/yandsearch?text="*.%s"&noreask=1&lr=193' % (self.site),).text
		#r = r.split('Нашлось<br>')[1].split('ответов</strong>')[0].strip()
		#print r
		return {
				'tyc': tyc, 'blogs': blog_links,
				'cat': 'YES' if xmldoc.getElementsByTagName('textinfo')[0].childNodes[0].nodeValue.strip() else 'NO',
		}

	def dmoz_rank(self):
		try:
			r = requests.get('http://www.dmoz.org/search?q=%s' % self.site, headers=self.headers).text
			return 'YES, %s' % (r.split('Open Directory Sites</strong>')[1].split(')</small>')[0].split(' of ')[1])
		except IndexError:
			return 'NO'

	def alexa_rank(self):
		r = requests.get('http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % self.site, headers=self.headers)
		xmldoc = parseString(r.text.encode('utf-8'))
		try:
			alexa = {
				'all_world': xmldoc.getElementsByTagName('POPULARITY')[0].attributes['TEXT'].value,
				'country': xmldoc.getElementsByTagName('COUNTRY')[-1].attributes['NAME'].value,
				'rank_in_country': xmldoc.getElementsByTagName('COUNTRY')[-1].attributes['RANK'].value,
			}
		except IndexError:
			alexa = {'all_world': 0, 'country': None, 'rank_in_country': None}
		return alexa

	def page_rank(self):
		"""
		#   Desc    :   Get PageRank of a Website, for Python
		#   Author  :   iSayme
		#   E-Mail  :   isaymeorg@gmail.com
		#   Website :   http://www.isayme.org
		#   Date    :   2012-08-04
		https://github.com/isayme/google_pr/blob/master/GooglePr.py
		"""
		gpr_hash_seed = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
		magic = 0x1020345
		for i in iter(range(len(self.site))):
			magic ^= ord(gpr_hash_seed[i % len(gpr_hash_seed)]) ^ ord(self.site[i])
			magic = (magic >> 23 | magic << 9) & 0xFFFFFFFF
		url = "http://toolbarqueries.google.com/tbr?client=navclient-auto&features=Rank&ch=%s&q=info:%s" % \
				("8%08x" % (magic), self.site)
		data = requests.get(url, headers=self.headers).text
		data = data.split(":") if data else None
		return int(data[len(data) - 1]) if data else 0

	def robots(self, data):
		r = requests.get("http://%s/%s" % (self.site, data), allow_redirects=False)
		return 'EMPTY' if r.status_code in [404, 301, 302] or r.text == self.html or '404' in r.text else r.text

	def index(self):
		google = requests.get("https://www.google.ru/search?q=site:%s" % self.site, headers=self.headers).text
		if 'ничего не найдено' in google:
			google = 0
		else:
			#.replace('примерно', '')
			try:
				google = google.split('id="resultStats">Результатов: ')[1].split('<')[0].replace('&#160;', '')
			except IndexError:
				google = 'CANT DETECT'
		yad_session = requests.Session()
		yandex = yad_session.get("http://yandex.ru/yandsearch?text=&site=%s&ras=1" % self.site, headers=self.headers)
		try:
			yandex = yandex.text.split('Нашлось<br>')[1].split('ответов</strong>')[0].replace('&nbsp;', ' ').strip()
		except IndexError:
			# TODO Yandex needs capcha
			yandex = 'NEED CAPTCHA'
		yad_ind = requests.get("http://webmaster.yandex.ru/check.xml?hostname=%s" % self.site, headers=self.headers)
		mirror_text = 'Сайт является зеркалом</span> '
		if mirror_text in yad_ind.text:
			mirror = yad_ind.text.split(mirror_text)[1].split(', ')[0]
			yad_ind = requests.get("http://webmaster.yandex.ru/check.xml?hostname=%s" % mirror, headers=self.headers)
		try:
			yad_ind = yad_ind.text.split('Страницы: ')[1].split('</div>')[0]
		except IndexError:
			yad_ind = 0
		# TODO DELETE Retries
		try:
			yahoo = requests.get('http://search.yahoo.com/search?ei=UTF-8&p=site:%s' % self.site,
							 headers=self.headers).text.split('<span>')[-1].split(' result')[0]
		except IndexError:
			yahoo = 0
		return {'google': google, 'yandex_standart': yandex, 'yandex_in_index': yad_ind, 'yahoo_index': yahoo}

	def bing_information(self, string):
		try:
			return requests.get('http://www.bing.com/search?q=%s%s' % (string, self.site),
						headers=self.headers).text.split('результаты: ')[1].split('</span>')[0].replace('&#160;', '')

		except IndexError:
			return 0

	def catalogs(self, string, catalog):
		return 'NO' if string in requests.get("%s%s" % (catalog, self.site), headers=self.headers).text else 'YES'

	def engine(self, string):
		r = requests.get('http://%s/%s' % (self.site, string), headers=self.headers, allow_redirects=True)
		return 'YES' if r.status_code not in [404, 403, 503, 301, 302] \
				and r.text != self.html and '404' not in r.text else 'NO'

	def who(self):
		# Не юзается "встроенная" whois, тк на unix она встроенная, на винде, говорят, нет
		r = requests.post("http://www.ripn.net/nic/whois/whois.cgi", {'Whois': self.site, 'Host': 'whois.ripn.net'},
			headers=self.headers, allow_redirects=True,).text.split('(in English).\n')[1].split('</PRE>')[0].strip()
		# http://www.ripn.net/about/servpol.html
		if 'You have exceeded allowed connection rate.' in r:
			return 'Вы сделали больше 30 запросов в минуту (лимит). Попробуйте позже'
		elif 'You are not allowed to connect' in r:
			return 'Вы в течении 15 минут превышали лимит (30 запросов в минуту). Восстановление доступа будет ' \
										'не менее, чем через час'
		else:
			return re.compile(r'<.*?>').sub('', r)

	def html_valid(self):
		r = requests.get('http://validator.w3.org/check?uri=%s' % self.site, headers=self.headers,).text
		r = r.split('valid">')[2].split('</td>')[0].strip()
		return re.compile(r'<.*?>').sub('', r) if '<' in r else r

	def find_meta_tags_content(self, meta_tag):
		"""
		Функция ищет в html коде сайта мета тег переданный ей и возвращает
		его значение. Функция учитывает возможность расположения параметра name
		после параметра content и до.
		
		Принимает:
			meta_tag - значение какого мета тега ищем - title, keywords, descriptions
		
		Возвращает:
			meta_tag_content - строка с содержанием мета-тега
		"""
		meta_tag_content = 'NO'
		match_meta_tag_str = re.compile(r'<meta[.\s\S]+?>', re.I)
		meta_tag_raws = re.findall(match_meta_tag_str, self.html)
		for raw in meta_tag_raws:
			if meta_tag in raw.lower():
				content_match = re.compile(r'content=(?:\'|\")([\s\S.]+)(?:\'|\")', re.I)
				if re.search(content_match, raw):
					meta_tag_content = re.search(content_match, raw).group(1)
		return meta_tag_content

	def __str__(self):
		if self.error:
			return str(self.error)
		else:
			return self.output.format(whois=self.whois, lines='='*50, ip=self.ip, web_server=self.web_server,
									powered_by=self.powered_by, content_lanuage=self.content_lanuage,
									content_type=self.content_type, title=self.title, description=self.description,
									key_words=self.key_words, html_validator=self.html_validator, tyc=self.yad['tyc'],
									pr=self.pr, all_world=self.alexa['all_world'], country=self.alexa['country'],
									rank_in_country=self.alexa['rank_in_country'], cat=self.yad['cat'],
									mail_catalog=self.mail_catalog, yahoo_catalog=self.yahoo_catalog, dmoz=self.dmoz,
									blogs=self.yad['blogs'], google=self.pro_index['google'],
									yandex_standart=self.pro_index['yandex_standart'], tdp=self.tdp_catalog,
									yandex_in_index=self.pro_index['yandex_in_index'], ya_metrica=self.ya_metrica,
									google_an=self.google_an, live_inet=self.live_inet, rambler_top=self.rambler_top,
									mail_rating=self.mail_rating, joomla=self.joomla, word_press=self.word_press,
									umi=self.umi, ucoz=self.ucoz, bitrix=self.bitrix, simple_login=self.simple_login,
									admin_login=self.admin_login, modx=self.modx, dle=self.dle, drupal=self.drupal,
									robots_txt=self.robots_txt, sitemap_xml=self.sitemap_xml,
									g_safe=self.safe_site['google'], yad_safe=self.safe_site['yandex'],
									yahoo_index=self.pro_index['yahoo_index'], bing_out=self.bing[0],
									bing_index=self.bing[1], all_time=self.all_time)

	def safebrowsing(self):
		# This site is not currently listed as suspicious.
		# this site has not hosted malicious software over the past 90 days
		g = requests.get('http://safebrowsing.clients.google.com/safebrowsing/diagnostic?site=%s' % self.site,
							headers=self.headers).text
		if 'is not currently listed':
			message = 'NO - В настоящее время этот сайт не занесен в список подозрительных.'
		else:
			message = 'YES - В настоящее время этот сайт занесен в список подозрительных.'  # may be, need test site
		if 'has not hosted malicious' in g:
			message = '%s NO - За последние 90 дней на этом сайте не размещалось вредоносное ПО.' % message
		else:
			message = '%s YES - За последние 90 дней на этом сайте размещалось вредоносное ПО.' % message
		yad = requests.get('http://yandex.ru/infected?l10n=ru&url=%s' % self.site,
								headers=self.headers).text.split('<title>')[1].split('</title>')[0].strip()
		return {'google': message, 'yandex': yad}


if __name__ == '__main__':
	print(SiteAuditor(input('Enter site, please: ')))