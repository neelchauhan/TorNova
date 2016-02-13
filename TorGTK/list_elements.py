from var import *
from ui_elements import *
from gi.repository import Gtk
from torctl import *

# ORGANIZATION OF THESE LISTS:
# 1. Main list for all the elements
# 2. A sublist for each element, with the first being a label, and the second
#    being the element itself

# List for main listbox
lb_main_elements = [
	["Enable Tor", init_switch("swEnable", enableTor)],
	["", init_button("btnLog", "Log", show_log_win)],
	["", init_button("btnAbout", "About", about_box)],
]

# List for settings listbox
lb_settings_elements = [
	["SOCKS Port", init_spinbutton("spinSocks", default_socks_port, 1024, 65535, 1)],
	["Control Port", init_spinbutton("spinCtl", default_control_port, 1024, 65535, 1)],
]
