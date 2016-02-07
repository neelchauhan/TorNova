import os
from var import *
from ui_elements import message_box, refresh_log
from gi.repository import Gtk
import stem.process
from stem.util import term
# Debug lines
import traceback
import sys

# Function to start Tor process
def startTor():
	tor_proc = None
	# Attempt to start Tor
	try:
		print("Logfile is at: " + tor_logfile_location)
		tor_proc = stem.process.launch_tor_with_config(
			config = {
				"SocksPort": str(objs["spinSocks"].get_text()),
				"ControlPort": str(objs["spinCtl"].get_text()),
				"Log": "Notice file " + tor_logfile_location,
			}
		)
	# Return error message
	except OSError as err_m:
		message_box(ErrorBox, "ERROR", str(err_m))
		objs["swEnable"].set_active(False)
	# Return process descriptor (mainly to close it)
	return tor_proc

# Function to kill Tor
def stopTor(tor_proc):
	if "kill" in dir(tor_proc):
		tor_proc.kill()

# Wrapper function for enabling/disabling Tor
def enableTor(switch, gparam):
	if switch.get_active():
		objs["lbSettings"].set_sensitive(False)
		global tor_process
		tor_process = startTor()
	else:
		objs["lbSettings"].set_sensitive(True)
		stopTor(tor_process)

# Wrapper function to kill application
def stopApp(*args):
	if objs["swEnable"].get_active():
		stopTor(tor_process)
	objs["swEnable"].set_active(False)
	if os.path.exists(tor_logfile_location):
		os.remove(tor_logfile_location)
	os.removedirs(tor_logfile_dir)
	Gtk.main_quit(*args)
