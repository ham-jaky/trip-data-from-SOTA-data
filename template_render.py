from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))


def render_sigle_section_tex(summit_dict):
	template = environment.get_template("single-section-de.jinja-latex")
	return template.render(summit_dict)

def render_multi_table_tex(*summits):
	data = {"summit_list": summits}
	template = environment.get_template("multi-table-de.jinja-latex")
	return template.render(data)
