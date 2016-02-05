from var import *
from gi.repository import Gtk

# Add GTK objects into dictionary (dictionary used to reference GTK objects)
def init_gtk_objects(builder):
	for obj in builder.get_objects():
		obj_name = Gtk.Buildable.get_name(obj)
		objs[obj_name] = builder.get_object(obj_name)

def init_switch(name, action):
	objs[name] = Gtk.Switch()
	objs[name].connect("notify::active", action)
	return objs[name]

def init_button(name, label, action):
	objs[name] = Gtk.Button.new_with_label(label)
	objs[name].connect("clicked", action)
	return objs[name]

def init_spinbutton(name, default_value, min_value, max_value, increment):
	objs[name] = Gtk.SpinButton()
	objs[name].set_numeric(True)
	adjustment = Gtk.Adjustment(default_value, min_value, max_value, increment, increment, 1)
	objs[name].set_adjustment(adjustment)
	return objs[name]

# Code to add row
def add_row(listbox, left, right):
	row = Gtk.ListBoxRow()
	hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
	row.add(hbox)
	hbox.pack_start(left, True, True, 0)
	hbox.pack_start(right, False, True, 0)

	objs[listbox].add(row)

# Code to turn listbox definition list into GTK ListBox rows
def listbox_addrow(listbox, row_list):
	for row in row_list:
		label = Gtk.Label(row[0], xalign=0)
		add_row(listbox, label, row[1])

# Code for message box
def message_box(mtype, title, message):
	dialog = Gtk.MessageDialog(objs["mainWindow"], 0, mtype, Gtk.ButtonsType.OK, title)
	dialog.format_secondary_text(message)
	dialog.run()
	dialog.destroy()

# Code for about box
def about_box(gparam):
	message_box(InfoBox, "About TorGTK 0.1.1", "Copyright 2016 Neel Chauhan. TorGTK is licensed under the Simplified BSD license.")
