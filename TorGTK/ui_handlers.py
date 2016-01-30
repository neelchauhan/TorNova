from gi.repository import Gtk
from torctl import enableTor
from ui_elements import msgAbout
# Define UI Handlers (Connect GTK events to Python functions)
handlers = {
	"windowDelete": Gtk.main_quit,
	"enableTor": enableTor,
	"msgAbout": msgAbout
}
