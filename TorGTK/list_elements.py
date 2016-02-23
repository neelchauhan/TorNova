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
	["", init_menubutton("btnMainMenu", objs["menuMain"])],
	["Enable Tor", init_switch("swEnable", enableTor)],
]

# List for settings listbox
lb_settings_elements = [
	["SOCKS Port", init_spinbutton("spinSocks", default_socks_port, 1024, 65535, 1)],
	["Control Port", init_spinbutton("spinCtl", default_control_port, 1024, 65535, 1)],
	["Exit Nodes", init_textfield("txtExit")],
	["Entry Nodes", init_textfield("txtEntry")],
]
