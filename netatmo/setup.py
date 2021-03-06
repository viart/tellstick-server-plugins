#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from setuptools import setup
	from setuptools.command.bdist_egg import bdist_egg
except ImportError:
	from distutils.core import setup
	from distutils.command.bdist_egg import bdist_egg
import os

class buildweb(bdist_egg):
	def run(self):
		print("generate web application")
		if os.system('npm install') != 0:
			raise Exception("Could not install npm packages")
		if os.system('npm run build') != 0:
			raise Exception("Could not build web application")
		bdist_egg.run(self)

setup(
	name='Netatmo Weather',
	version='1.1',
	author='Telldus Technologies AB',
	author_email='info.tech@telldus.se',
	category='weather',
	description='Use Netatmo weather station in Telldus Live!',
	long_description="""
		Use this plugin to collect weatherdata from your Netatmo weather station
		Data is imported every 10 minutes.
		You'll need to connect your Netatmo accout in the settings for the plugin.
	""",
	icon='netatmo-weather.png',
	color='#388cbf',
	packages=['netatmo'],
	package_dir = {'':'src'},
	cmdclass={'bdist_egg': buildweb},
	entry_points={ \
		'telldus.startup': ['c = netatmo:Netatmo [cREQ]']
	},
	extras_require = dict(cREQ = 'Base>=0.1\nTelldus>=0.1\nTelldusWeb>=0.1'),
	package_data={'netatmo' : [
		'htdocs/*.js',
	]}
)
