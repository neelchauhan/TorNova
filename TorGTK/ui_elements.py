from var import *
from gi.repository import Gtk

# Add GTK objects into dictionary (dictionary used to reference GTK objects)
def init_gtk_objects(builder):
	for obj in builder.get_objects():
		obj_name = Gtk.Buildable.get_name(obj)
		objs[obj_name] = builder.get_object(obj_name)

# Code for message box
def message_box(mtype, title, message):
	dialog = Gtk.MessageDialog(objs["mainWindow"], 0, mtype, Gtk.ButtonsType.OK, title)
	dialog.format_secondary_text(message)
	dialog.run()
	dialog.destroy()

# Code for about box
def msgAbout(gparam):
	message_box(InfoBox, "About TorGTK 0.1.0", "Copyright 2016 Neel Chauhan. TorGTK is licensed under the Simplified BSD license.")
