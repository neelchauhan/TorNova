#!/usr/bin/env python

from setuptools import setup
import sys

setup(name="TorGTK",
	version="0.2.2",
	description="GTK3 Frontend for Tor",
	license = "BSD",
	author="Neel Chauhan",
	author_email="neel@neelc.org",
	url="https://www.github.com/neelchauhan/TorGTK/",
	packages=["TorGTK"],
	entry_points={'gui_scripts': ['NovaTor=NovaTor.main:main_loop']},
	package_data={"NovaTor": ["data/*"]},
	install_requires=[
		"stem",
	],
	data_files=[
		(sys.prefix + "/share/pixmaps", ["icons/scalable/novator.svg"]),
		(sys.prefix + "/share/applications", ["data/novator.desktop"]),
	],
	classifiers=[
		"Environment :: X11 Applications :: GTK",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: BSD License",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 2",
	],
)
