import pkg_resources
import os.path
import os

# Code to detect filename
def detect_filename(filename):
	if os.path.isfile(filename):
		return filename
	else:
		return pkg_resources.resource_filename(__name__, filename)

# Code to make directory if it doesn't exist
def make_dir_if_not_exist(path):
	if not os.path.exists(path):
		os.makedirs(path)
