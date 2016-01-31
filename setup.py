#!/usr/bin/env python

from setuptools import setup

setup(name="TorGTK",
	version="0.1.0",
	description="GTK3 Frontend for Tor",
	license = "BSD",
	author="Neel Chauhan",
	author_email="neel@neelc.org",
	url="https://www.github.com/neelchauhan/TorGTK/",
	packages=["TorGTK"],
	entry_points={'gui_scripts': ['TorGTK=TorGTK.main:main_loop']},
	package_data={"TorGTK": ["data/*"]},
	install_requires=[
		"stem",
	],
	classifiers=[
		"Environment :: X11 Applications :: GTK",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: BSD License",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 2",
	],
)
