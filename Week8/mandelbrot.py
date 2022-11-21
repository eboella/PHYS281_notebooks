#!/usr/bin/env python

# Little program for plotting the Mandelbrot set.  Uses a package
# called tkinter to create a "canvas" inside a window, on which we
# plot points.

import tkinter


def in_set(x,y,maxits=100):
    """Decide whether or not a point c=x+i.y in the Argand plane lies in the
    Mandelbrot set.  Starting from z_0=c, iteratively update z as
    z_{n+1}=z_n^2+c.  c is in the Mandelbrot set if and only if this sequence
    does not diverge.  If |z_n|>2 then we know that the sequence diverges.
    Check the first maxits terms in the sequence to see if |z_n|>2."""
    c=complex(x,y)
    z=c # Initial value of z.
    for _i in range(maxits):
        z=z*z+c # Iteration scheme for z.
        if abs(z)>2.0:
            return False # c=x+i.y is definitely not in the set.
    return True # Have not shown that the point c=x+i.y is not in the set.


# Create a Tk instance.
root=tkinter.Tk()
# Halt if the window is closed.
root.protocol("WM_DELETE_WINDOW",root.quit())

# Create a square canvas whose side length is the minimum of the
# number of pixels in the x and y directions.
npixels=int(0.80*min(root.winfo_screenwidth(),root.winfo_screenheight()))
canvas=tkinter.Canvas(root,width=npixels,height=npixels)
canvas.pack()

# Range of x (real part) and y (imaginary part) to include in plot.
# Alter the sidelength, xmin and ymin to zoom in on a particular
# place.  If you zoom in a lot, you will probably need to increase
# maxits in function in_set, otherwise you will get a lot of points
# that are incorrectly reported to be in the Mandelbrot set.  However,
# it will then take longer to run.
sidelength=3.0
xmin=-2.0 ; xmax=xmin+sidelength
ymin=-1.5 ; ymax=ymin+sidelength

# Distance between points in the x and y directions (fixed to be the same
# because we are looking at a square region).
dx=sidelength/float(npixels)  ;  dy=dx

# Loop over points to test.  If they are in the Mandelbrot set then draw a
# point (actually a little line) on the canvas.
x=xmin
for ix in range(npixels):
    y=ymin
    for iy in range(npixels):
        if in_set(x,y):
            _=canvas.create_line(ix,iy,ix+1,iy+1,fill="#000000")
        y+=dy
    root.update() # Update the canvas after each loop over y.
    x+=dx

root.mainloop() # Wait for the user to close the window.

# Suggested extensions (increasingly challenging):

# * Manually adjust the plot region (sidelength, xmin and ymin) to
#   zoom in on some pretty regions of the set, and then rerun the
#   program.  What happens if you zoom in too far?  How can you
#   restore the accuracy of the plot?

# * Modify function in_set so that it returns the number of iterations
#   required to reach |z|>2 (or, say, a negative integer if the point
#   being tested lies in the Mandelbrot set).  Use these results to
#   plot different colours for points that are not in the set.

# * Allow the user to drag and select a "zoom square" with the mouse
#   pointer (will need to look up event handling in tkinter), and then
#   redraw the set for that region.

# * (For experts) Make the code faster!  Rewrite the expensive parts
#   in C or Fortran and parallelise them.
