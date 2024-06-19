"""
beNNch-plot - standardized plotting routines for performance benchmarks.
Copyright (C) 2021 Forschungszentrum Juelich GmbH, INM-6

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.

SPDX-License-Identifier: GPL-3.0-or-later
"""

"""
Default parameters for plotting
"""
import tol_colors

size_factor = 1.3
matplotlib_params = {
    'text.latex.preamble': ['\\usepackage{gensymb}'],
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'axes.grid': False,
    'axes.labelsize': 15 * size_factor,
    'axes.titlesize': 19 * size_factor,
    'font.size': 16 * size_factor,
    'legend.fontsize': 11 * size_factor,
    'xtick.labelsize': 11 * size_factor,
    'ytick.labelsize': 11 * size_factor,
    'text.usetex': False,
}

additional_params = {
    'figsize_single': [6.1 * 1.5, 6.1],
    'figsize_double': [12.2, 6.1 * 1.1]
}

bright = tol_colors.tol_cset('bright')
vibrant = tol_colors.tol_cset('vibrant')
light = tol_colors.tol_cset('light')

color_params = {
    'wall_time_total': light.pale_grey,
    'sim_factor': light.pink,
    'phase_total_factor': light.orange,
    'time_simulate': light.pink,
    'time_construction_create+time_construction_connect': light.light_cyan,
    'time_update_spike_data': light.orange,
    'time_deliver_spike_data': light.light_blue,
    'time_communicate_spike_data': light.mint,
    'wall_time_phase_collocate': light.light_yellow,
    'frac_phase_update': light.orange,
    'frac_phase_deliver': light.light_blue,
    'frac_phase_communicate': light.mint,
    'frac_phase_collocate': light.light_yellow,
    'phase_update_factor': light.orange,
    'phase_deliver_factor': light.light_blue,
    'phase_communicate_factor': light.mint,
    'phase_collocate_factor': light.light_yellow,
    'total_memory': light.olive,
    'total_memory_per_node': light.pear,
}

label_params = {
    'threads_per_node': 'OMP threads',
    'tasks_per_node': 'MPI processes',
    'num_nodes': 'Nodes',
    'wall_time_total': 'Total',
    'wall_time_preparation': 'Preparation',
    'wall_time_presim': 'Presimulation',
    'wall_time_creation': 'Creation',
    'wall_time_connect': 'Connection',
    'time_simulate': 'State propagation',
    'wall_time_phase_total': 'All phases',
    'time_update_spike_data': 'Update',
    'wall_time_phase_collocate': 'Collocation',
    'time_communicate_spike_data': 'Communication',
    'time_deliver_spike_data': 'Delivery',
    'time_construction_create+time_construction_connect': 'Network construction',
    'max_memory': 'Memory',
    'sim_factor': 'State propagation',
    'frac_phase_update': 'Update',
    'frac_phase_communicate': 'Communication',
    'frac_phase_deliver': 'Delivery',
    'frac_phase_collocate': 'Collocation',
    'phase_update_factor': 'Update',
    'phase_communicate_factor': 'Communication',
    'phase_deliver_factor': 'Delivery',
    'phase_collocate_factor': 'Collocation',
    'phase_total_factor': 'All phases',
    'total_memory': 'Memory',
    'total_memory_per_node': 'Memory per node',
}
