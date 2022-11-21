#!/usr/bin/env python

# Example Python script that uses matplotlib to plot the tanh function.

# Note that there are lots of examples of clever things you can do and
# plots you can make with matplotlib at

#    https://matplotlib.org/stable/gallery/index.html

# Here I focus on doing a good job of making basic plots.

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# WHY OH WHY ARE THE DEFAULT FONT SIZES IN GRAPHING PROGRAMS,
# INCLUDING MATPLOTLIB, ALWAYS FAR TOO SMALL?

# It is necessary to increase the font size to make axis labels
# legible when figures are included in documents.

# In many undergraduate reports, PhD theses and manuscripts submitted
# to journals, the axis labels are microscopic.  Not good.

# There are several ways of setting default font sizes, etc., in matplotlib.

# 1. You can specify font size every time you add an axis label, etc.

# 2. You can set default behaviour at the top of your script file
# using the matplotlib.rc function:

mpl.rc('font',size=18)
mpl.rc('lines',linewidth=4,marker='',markersize=6,markeredgewidth=3)
mpl.rc('errorbar',capsize=6)
mpl.rc('axes',linewidth=3,grid=False)
mpl.rc('xtick.major',size=10,width=3)
mpl.rc('xtick.minor',visible=False,size=5,width=3)
mpl.rc('ytick.major',size=10,width=3)
mpl.rc('ytick.minor',visible=False,size=5,width=3)

# 3. You can place defaults in a "matplotlibrc" file, which is held
# either in the directory containing the script, or in a location
# specified by the MATPLOTLIBRC environment variable, or
# $HOME/.config/matplotlib/ (on Linux/Unix and probably also Mac) or
# .matplotlib (on Windows).  See

# https://matplotlib.org/stable/tutorials/introductory/customizing.html

# The advantage of options 1 & 2 is that you can send your script
# whatever.py to somebody else and it will work out of the box.  If
# you use option 3, you will also have to send them your matplotlibrc
# file.

# The advantage of option 3 is that you can set up your matplotlibrc
# file on your machine and then automatically get your customised
# setup, at least on that machine, without any further thought.

# Create a figure object.
fig=plt.figure()

# Add subplot 1 of a 1x1 array of plots.
ax=fig.add_subplot(1,1,1)

# Use np.arange to create a NumPy array of values from -6.0 to 6.0, with
# the spacing of the points being 0.01.
xx=np.arange(-6.0,6.0,0.01)

# Numpy functions are "elemental" functions, meaning that you can give
# a function an array as an argument, and the function will be applied
# element-wise to the array.  Hence np.tanh(xx) is an array containing
# hyperbolic tangent values, corresponding to xx.
yy=np.tanh(xx)

# Plot yy against xx.  Colour: red.  Linestyle: solid line.
# Label: uses TeX commands.  Use a raw string (r"whatever") to avoid problems
# with backslashes in TeX commands.
ax.plot(xx,yy,c='r',ls="-",label=r"$y=\tanh(x)$")

# Add a second line to the plot.  Avoid relying on distinctions
# between red and green: this is the most common colour-blindness.
yy=np.tanh(2.0*xx)
ax.plot(xx,yy,c='b',ls=":",label=r"$y=\tanh(2x)$")

# Load some data from a text file holding three columns: x data, y
# data and error bars on the y data.

xx,yy,err_yy=np.loadtxt("example_data.dat",unpack=True)

ax.errorbar(xx,yy,err_yy,label="Example data",ls="",marker="o",c="k")

# Axes always need labels.  If plotting physical quantities then you
# should always give the correct units.  If you want your axis labels,
# etc., to look more professional, use TeX math mode for mathematical
# symbols.
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

# Add a legend (label which curve is which).  Override the default font size,
# so the legend fits on the graph (but is still big enough).
ax.legend(fontsize=15)

# Adjust the padding around subplots.
plt.tight_layout()

# Show the plot in an interactive manner.
plt.show()

# Write out the plot as a PDF file, which you can incorporate into a
# TeX document using \includegraphics.
#plt.savefig("tanh.pdf",transparent=True)

# Finally close the plot.
plt.close()
