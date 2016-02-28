from gi.repository import Gtk
from torctl import enableTor, stopApp, refresh_log
# Define UI Handlers (Connect GTK events to Python functions)
handlers = {
	"windowDelete": stopApp,
	"enableTor": enableTor,
}
