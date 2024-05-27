#!/usr/bin/env python3
import template_render
import sota_data


def some_tests():
	print(template_render.render_multi_table_tex(sota_data.test_summit_single))
#	print(template_render.render_sigle_section_tex(sota_data.test_summit_single))


def main():
	print("Nothing to see here. ¯\_(ツ)_/¯")
	some_tests()


if __name__ == "__main__":
	main()
