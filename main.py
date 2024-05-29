#!/usr/bin/env python3
import template_render
import sota_data


def some_tests():
	x, y = sota_data.load_csv()
	print(y)
	data = sota_data.refs_in_list(x, ["DM/HE-001", "DM/HE-007", "DM/HE-017", "DM/HE-111", "DM/BM-241", "DM/TH-001", "DM/TH-414", "DM/TH-853"])

	with open("test.txt", "w", encoding="utf-8") as f:
		f.write(template_render.render_multi_table_tex(*data))
#	print(template_render.render_sigle_section_tex(sota_data.test_summit_single))


def main():
	print("Nothing to see here. ¯\_(ツ)_/¯")
	some_tests()


if __name__ == "__main__":
	main()
	print("Done ╰(*°▽°*)╯")
