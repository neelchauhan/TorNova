from gi.repository import Gtk
import tempfile
import os.path

# Define default port numbers
default_socks_port = 19050
default_control_port = 19051

# Tor process descriptor placeholder
tor_process = None

# Tor logfile location placeholder
tor_logfile_dir = tempfile.mkdtemp()
tor_logfile_location = os.path.join(tor_logfile_dir, "tor_log")

# User preferences location placeholder
home_dir = os.path.expanduser("~")
prefs_dir = os.path.join(home_dir, ".local", "share", "torgtk")

# Define object dictionary
objs = { }

# Define error message types
InfoBox = Gtk.MessageType.INFO
ErrorBox = Gtk.MessageType.ERROR
