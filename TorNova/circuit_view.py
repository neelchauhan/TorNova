from gi.repository import Gtk
from var import *
from ui_elements import *
from stem import CircStatus
from stem.control import Controller
import time

def set_circuits():
	while objs["swEnable"].get_active():
		with Controller.from_port(port = int(objs["spinCtl"].get_text())) as controller:
			controller.authenticate()

			for circ in sorted(controller.get_circuits()):
				if circ.status != CircStatus.BUILT:
					continue

				exp_name = "expCirc" + str(circ.id)
				lbl_name = "lblCirc" + str(circ.id)
				if exp_name not in objs:
					exp_lbl = "Circuit " + str(circ.id)
					init_expander(exp_name, exp_lbl)

					circ_str = ""
					iter = 0
					for i, entry in enumerate(circ.path):
						fingerprint, nickname = entry
						desc = controller.get_network_status(fingerprint, None)
						address = desc.address if desc else "unknown"
						if iter == 0:
							circ_str += "Entry: "
						elif iter == 1:
							circ_str += "Middle: "
						elif iter == 2:
							circ_str += "Exit: "

						circ_str += (fingerprint + "(" + nickname + ", " + address + ")")
						circ_str += "\n"
						iter += 1
					circ_str = circ_str[:len(circ_str)-1]
					init_label(lbl_name, circ_str)
					add_to_expander(exp_name, lbl_name)
					add_srow("lbCircuit", objs[exp_name])
		time.sleep(1)
