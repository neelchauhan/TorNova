from gi.repository import Gtk
from torctl import enableTor, stopApp
# Define UI Handlers (Connect GTK events to Python functions)
handlers = {
	"windowDelete": stopApp,
	"enableTor": enableTor,
}
