#!/usr/bin/python3
# -*- coding: utf-8 -*-
from distutils.core import setup
import os
import sys
import site_auditor

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()


def open_docs(doc):
	with open(doc, encoding="utf8") as f:
		return f.read()

setup(
	name=site_auditor.__title__,
	version=site_auditor.__version__,
	description='site auditor',
	long_description=open_docs('README.rst') + '\n\n' + open_docs('HISTORY.rst'),
	packages=['site_auditor'],
	package_dir={'site_auditor': 'site_auditor'},
	#zip_safe=False,
	url='https://github.com/stleon/OmgSite',
	download_url='https://github.com/stleon/OmgSite/archive/master.zip',
	license=site_auditor.__license__,
	author='ST LEON',
	author_email='leonst998@gmail.com',
	maintainer='ST LEON',
	maintainer_email='leonst998@gmail.com',
	requires=['requests'],
	platforms='any',
	#install_requires=['requests'],
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: Russian',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.3',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Internet :: WWW/HTTP :: Site Management',
		'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
],
)