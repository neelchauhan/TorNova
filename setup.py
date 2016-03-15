#!/usr/bin/env python

from setuptools import setup
import sys

setup(name="TorNova",
	version="0.2.3",
	description="GTK3 Frontend for Tor",
	license = "BSD",
	author="Neel Chauhan",
	author_email="neel@neelc.org",
	url="https://www.github.com/neelchauhan/TorGTK/",
	packages=["TorNova"],
	entry_points={'gui_scripts': ['TorNova=TorNova.main:main_loop']},
	package_data={"TorNova": ["data/*"]},
	install_requires=[
		"stem",
	],
	data_files=[
		(sys.prefix + "/share/pixmaps", ["icons/scalable/tornova.svg"]),
		(sys.prefix + "/share/applications", ["data/tornova.desktop"]),
	],
	classifiers=[
		"Environment :: X11 Applications :: GTK",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: BSD License",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 2",
	],
)
