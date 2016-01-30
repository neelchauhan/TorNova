from gi.repository import Gtk

# Define default port numbers
default_socks_port = 19050
default_control_port = 19051

# Tor process descriptor placeholder
tor_process = None

# Define object dictionary
objs = { }

# Define error message types
InfoBox = Gtk.MessageType.INFO
ErrorBox = Gtk.MessageType.ERROR
