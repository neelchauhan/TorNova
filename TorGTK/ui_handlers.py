from gi.repository import Gtk
from torctl import enableTor, stopApp
from ui_elements import msgAbout
# Define UI Handlers (Connect GTK events to Python functions)
handlers = {
	"windowDelete": stopApp,
	"enableTor": enableTor,
	"msgAbout": msgAbout,
}
