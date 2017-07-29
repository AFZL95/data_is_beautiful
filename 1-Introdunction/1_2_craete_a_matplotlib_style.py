import matplotlib as mpl
# you can see where the "already bulit in styles" are located by command below :
# mpl.get_configdir()
# so then you know where is it ! 
# for instance it is in the '/Users/FZL/.matplotlib'

# then you create a python file and customize your prefered style with rcParams like below

custom_style = '''
figure.figsize: 12, 7
figure.edgecolor: white
figure.facecolor: white

lines.linewidth: 2.5
lines.markeredgewidth: 0
lines.markersize: 10
lines.dash_capstyle: butt

legend.fancybox: True

font.size: 14

axes.color_cycle: 1f77b4, ff7f0e, 2ca02c, d62728, 9467bd, 8c564b, e377c2, 7f7f7f, bcbd22, 17becf
axes.linewidth: 0
axes.titlesize: 22
axes.labelsize: 16

xtick.labelsize: 14
ytick.labelsize: 14
xtick.major.size: 0
xtick.minor.size: 0
ytick.major.size: 0
ytick.minor.size: 0

axes.grid: True
grid.alpha: 0.3
grid.linewidth: 0.5
grid.linestyle: --
grid.color: black

savefig.transparent: False
savefig.bbox: tight
savefig.format: png
'''

mpl_style_location = ('{}/stylelib/my_custom_style.mplstyle'.format(mpl.get_configdir()))

with open(mpl_style_location, 'w') as out_file:
    out_file.write(custom_style)



# then you must reload the matplotlibe style library
# plt.style.reload_library()

# and finally it would be added to your matplotlib available styles:
# plt.style.available