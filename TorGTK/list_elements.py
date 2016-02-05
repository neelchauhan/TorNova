from var import *
from ui_elements import *
from gi.repository import Gtk
from torctl import *

lb_main_elements = [
	["Enable Tor", init_switch("swEnable", enableTor)],
	["", init_button("btnAbout", "About", about_box)],
]

lb_settings_elements = [
	["SOCKS Port", init_spinbutton("spinSocks", default_socks_port, 1024, 65535, 1)],
]
