import re

def xnot(exp1, exp2):
	if exp1 == exp2:
		return True
	else:
		return False;

def parse_node_select(string, exclude_nodes):
	# Compile regular expressions
	space_reg = re.compile(r"[^a-zA-Z0-9- ]")
	strip_str = space_reg.sub("", string);
	lst = re.split("[ ,]+", strip_str)

	out_lst = []

	# Parse elements and sort them
	for item in lst:
		match_str = item
		exclude = False
		out_str = None

		if item[0] == '-':
			match_str = item[1:]
			exclude = True

		if len(match_str) == 40:
			out_str = "$" + match_str
		elif len(match_str) == 2:
			out_str = "{" + match_str + "}"

		if xnot(exclude_nodes, exclude):
			out_lst.append(out_str)

	# Return dictionary
	return out_lst
