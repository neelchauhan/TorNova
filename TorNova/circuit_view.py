from gi.repository import Gtk
from var import *
from ui_elements import *

def set_circuits():
	init_expander("expSample", "Sample Circuit")
	init_label("lbl1", "Hello!")
	add_to_expander("expSample", "lbl1")
	add_srow("lbCircuit", objs["expSample"])
