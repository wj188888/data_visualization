# -*- coding: utf-8 -*-

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['public-apis', 'system-design-primer', 'thefuck']
plot_dicts = [
    {'value': 171348, 'label': 'Description of public-apis'},
    {'value': 116766, 'label': 'Description of system-design-primer'},
    {'value': 69892, 'label': 'Description of thefuck'}
]
chart.add('', plot_dicts)
chart.render_to_file('../statics/bar_descriptions.svg')