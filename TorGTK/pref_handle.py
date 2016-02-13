import ConfigParser
from gi.repository import Gtk
from pref_mapping import *
from var import *

def write_config(filename):
	# Open file
	config_fd = open(filename, "w")

	Config = ConfigParser.ConfigParser()
	Config.add_section("TorGTKprefs")
	# Write sections to file and close it
	for key in pref_mappings:
		Config.set("TorGTKprefs", key, objs[pref_mappings[key]].get_text())
	Config.write(config_fd)
	config_fd.close()
