#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from var import *
from torctl import *
from fn_handle import *
from list_elements import *
from menu_elements import *
from ui_elements import *
from ui_handlers import *

# Add Glade files
builder = Gtk.Builder()
builder.add_from_file(detect_filename("data/main_window.glade"))
builder.add_from_file(detect_filename("data/log_window.glade"))
builder.add_from_file(detect_filename("data/settings_window.glade"))

# Add GTK objects into dictionary (dictionary used to reference GTK objects)
init_gtk_objects(builder)

# Main loop
def main_loop(args=None):
	make_dir_if_not_exist(prefs_dir)
	read_config_if_exists(prefs_file)

	builder.connect_signals(handlers)

	listbox_addrow("lbMain", lb_main_elements)
	listbox_addrow("lbSettings", lb_settings_elements)

	objs["mainWindow"].set_wmclass("TorNova", "TorNova")
	objs["mainWindow"].show_all()
	objs["mainWindow"].set_title("TorNova")

	menu_compile("menuMain", menu_main_elements)

	Gtk.main()

# Namespace main loop
if __name__ == "__main__":
	main_loop()
