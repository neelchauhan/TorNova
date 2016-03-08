from gi.repository import Gtk
from var import *
from ui_elements import refresh_log
import time

def update_log_interval():
	while objs["swEnable"].get_active():
		refresh_log(1)
		time.sleep(1)
