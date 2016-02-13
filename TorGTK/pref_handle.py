import ConfigParser
from gi.repository import Gtk
from pref_mapping import *
from var import *

def read_config_if_exists(filename):
	if os.path.isfile(filename):
		# Init config parser and read config
		Config = ConfigParser.SafeConfigParser()
		Config.read(filename)
		section = "TorGTKprefs"

		# Loop through options
		options = Config.options(section)
		for option in options:
			value = Config.get(section, option)
			objs[pref_mappings[option]].set_value(int(value))

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
