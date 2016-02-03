#!/usr/bin/env python
from gi.repository import Gtk
from var import *
from torctl import *
from fn_handle import detect_filename
from ui_elements import *
from ui_handlers import *

# Add Glade files
builder = Gtk.Builder()
builder.add_from_file(detect_filename("data/TorGTK-tabbed.glade"))

# Add GTK objects into dictionary (dictionary used to reference GTK objects)
init_gtk_objects(builder)

# Main loop
def main_loop(args=None):
	builder.connect_signals(handlers)

	label = Gtk.Label("SOCKS Port", xalign=0)
	objs["spinSocks"] = Gtk.SpinButton()
	objs["spinSocks"].set_numeric(True)
	adjustment = Gtk.Adjustment(default_socks_port, 1024, 65535, 1, 1, 1)
	objs["spinSocks"].set_adjustment(adjustment)
	add_row("lbSettings", label, objs["spinSocks"])

	label = Gtk.Label("Enable Tor", xalign=0)
	init_switch("swEnable", enableTor)
	add_row("lbMain", label, objs["swEnable"])

	objs["mainWindow"].set_wmclass("TorGTK", "TorGTK")
	objs["mainWindow"].show_all()
	objs["mainWindow"].set_title("TorGTK")

	Gtk.main()

# Namespace main loop
if __name__ == "__main__":
	main_loop()
