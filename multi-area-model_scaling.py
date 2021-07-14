import benchplot as bp
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec


args = {
    'data_hash': '21786536-dfd4-437b-9d43-f0c23e5ccea3',
    'data_path': './timing_results',
    'catalogue_path': 'catalogue.yaml',
    'manually_set_plot_name': 'MAM node scaling',
    'x_axis': ['num_nodes'],
    'time_scaling': 1e3
}
# args = {
#     'data_hash': 'fda5d63a-5648-4a0d-b180-f3633b33cbcf',
#     'data_path': './timing_results',
#     'catalogue_path': 'catalogue.yaml',
#     'manually_set_plot_name': 'MAM node scaling',
#     'x_axis': ['num_nodes'],
#     'time_scaling': 1e3
# }


# Instantiate class
B = bp.BenchPlot(**args)

# Plotting
widths = [1, 1]
heights = [3, 1]
fig = plt.figure(figsize=(12, 6), constrained_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig, width_ratios=widths,
                         height_ratios=heights)

ax1 = fig.add_subplot(spec[:, 0])
ax2 = fig.add_subplot(spec[0, 1])
ax3 = fig.add_subplot(spec[1, 1])


B.plot_fractions(axis=ax1,
                 fill_variables=['wall_time_sim',
                                 'wall_time_create+wall_time_connect'],
                 interpolate=True,
                 step=None,
                 error=True)
B.plot_main(quantities=['sim_factor', 'phase_total_factor'], axis=ax2)
B.plot_fractions(axis=ax3,
                 fill_variables=[
                     'frac_phase_communicate',
                     'frac_phase_update',
                     'frac_phase_deliver',
                     'frac_phase_collocate'
                     ])

ax1.set_xlabel('Number of Nodes')
ax1.set_ylabel('wall time [s]')
ax2.set_ylabel(r'real-time factor $T_{\mathrm{wall}}/$'
               r'$T_{\mathrm{model}}$')
ax3.set_xlabel('Number of Nodes')

# ax2.set_ylim((30,180))

ax1.legend()
B.merge_legends(ax2, ax3)
plt.savefig('metastable_JURECA.pdf')