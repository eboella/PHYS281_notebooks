#!/usr/bin/env python

# Little program for plotting the Mandelbrot set.

import tkinter as tk
import sys
try:
  import fmandel
except ImportError:
  sys.exit('This program requires the fmandel module.  Compile it by typing '
           '"make".')


class mandelplot():
  """Class for creation and display of image of Mandelbrot set."""

  def __init__(self):
    self.root=tk.Tk() # GUI
    self.root.protocol("WM_DELETE_WINDOW",self.root.quit())
    self.root.winfo_toplevel().title("Mandelbrot set")
    self.coordtext=tk.Text(self.root,height=1,width=90)
    self.coordtext.pack(side="bottom",anchor=tk.SW)
    self.npixels=int(0.95*min(self.root.winfo_screenwidth(),
                              self.root.winfo_screenheight()))
    self.root.bind('<Button-1>',self.leftbutton)
    self.root.bind('<Button-2>',self.middlebutton)
    self.root.bind('<Button-3>',self.rightbutton)
    self.root.bind('<B1-Motion>',self.drag)
    self.root.bind('<ButtonRelease-1>',self.releaseleftbutton)
    self.root.canvas=tk.Canvas(self.root,width=self.npixels,height=self.npixels)
    self.root.canvas.pack()
    self.cxmin=-2.0 ; self.cxmax=1.0 # Range of x values in plot region.
    self.cymin=-1.5 ; self.cymax=1.5 # Range of y values in plot region.
    self.xa=0 ; self.ya=0 # Anchor for zoom box.
    self.t=None # Bitmap image of Mandelbrot set
    self.zoombox=None
    self.coordtext.insert(tk.END,self.coordstotext(self.cxmin,self.cymin,
                                                   self.cxmax,self.cymax))
    self.plot_set()

  def plot_set(self):
    """Create and add new image of the Mandelbrot set."""
    if self.t:
      self.root.canvas.delete(self.t)
    self.t=tk.PhotoImage(width=self.npixels,height=self.npixels)
    self.t.put(fmandel.gen_mandelstring(self.npixels,self.npixels,self.cxmin,
                                        self.cxmax,self.cymin,self.cymax),
               (0,0,self.npixels-1,self.npixels-1))
    self.root.canvas.create_image(0,0,image=self.t,anchor=tk.NW)

  def zoomout(self,x,y,factor):
    """Zoom out, centred on (x,y), by given factor."""
    cxmid=self.cxmin+float(x)/float(self.npixels-1)*(self.cxmax-self.cxmin)
    cymid=self.cymin+float(self.npixels-1-y)/float(self.npixels-1)\
      *(self.cymax-self.cymin)
    chalflen=factor*0.5*max(self.cxmax-self.cxmin,self.cymax-self.cymin)
    self.cxmin=cxmid-chalflen ; self.cxmax=cxmid+chalflen
    self.cymin=cymid-chalflen ; self.cymax=cymid+chalflen
    self.plot_set()

  def leftbutton(self,event):
    """Handle left mouse button.  Start zoom box."""
    self.xa=event.x ; self.ya=event.y

  def rightbutton(self,event):
    """Handle right mouse button.  Zoom out."""
    self.zoomout(event.x,event.y,2.0)

  def middlebutton(self,event):
    """Handle middle mouse button.  Zoom out."""
    self.zoomout(event.x,event.y,10.0)

  def drag(self,event):
    """Handle dragging of zoombox."""
    xmin,ymin,xmax,ymax=self.squarebox(self.xa,self.ya,event.x,event.y)
    cxminp,cyminp,cxmaxp,cymaxp\
      =self.scaletoargand(xmin,ymin,xmax,ymax,self.npixels,self.cxmin,
                          self.cymin,self.cxmax,self.cymax)
    if self.zoombox:
      self.root.canvas.delete(self.zoombox)
    self.zoombox=self.root.canvas.create_rectangle(xmin,ymin,xmax,ymax,width=2,
                                                   outline='#fff')
    self.coordtext.delete('1.0',tk.END)
    self.coordtext.insert(tk.END,self.coordstotext(cxminp,cyminp,cxmaxp,cymaxp))

  def releaseleftbutton(self,event):
    """Handle release of left mouse button.  Zoom into zoombox region."""
    if 0<event.x<self.npixels and 0<event.y<self.npixels:
      xmin,ymin,xmax,ymax=self.squarebox(self.xa,self.ya,event.x,event.y)
      self.cxmin,self.cymin,self.cxmax,self.cymax\
        =self.scaletoargand(xmin,ymin,xmax,ymax,self.npixels,self.cxmin,
                            self.cymin,self.cxmax,self.cymax)
      self.root.canvas.delete(self.t)
      self.plot_set()
    self.root.canvas.delete(self.zoombox)

  def mainloop(self):
    """Tk mainloop."""
    self.root.mainloop()

  @staticmethod
  def squarebox(xa,ya,xb,yb):
    """Take two pairs of coordinates, the first of which is an "anchor", and
    return xmin, xmax, ymin, ymax."""
    l=max(min(abs(xb-xa),abs(yb-ya)),1)
    if xb>xa:
      xmin=xa ; xmax=xa+l
    else:
      xmax=xa ; xmin=xa-l
    if yb>ya:
      ymin=ya ; ymax=ya+l
    else:
      ymax=ya ; ymin=ya-l
    return xmin,ymin,xmax,ymax

  @staticmethod
  def scaletoargand(xmin,ymin,xmax,ymax,npixels,cxmin,cymin,cxmax,cymax):
    """Scale a pair of points in the grid to a point in the Argand plane."""
    cxminp=cxmin+float(xmin)/float(npixels-1)*(cxmax-cxmin)
    cxmaxp=cxmin+float(xmax)/float(npixels-1)*(cxmax-cxmin)
    cyminp=cymin+float(npixels-1-ymax)/float(npixels-1)*(cymax-cymin)
    cymaxp=cymin+float(npixels-1-ymin)/float(npixels-1)*(cymax-cymin)
    return cxminp,cyminp,cxmaxp,cymaxp

  @staticmethod
  def coordstotext(cxmin,cymin,cxmax,cymax):
    """Turn coordinates of rectangle into a string to print."""
    return "({0:.16g},{1:.16g}) -> ({2:.16g},{3:.16g})"\
      .format(cxmin,cymin,cxmax,cymax)


# Main program starts here.
if __name__=='__main__':
  m=mandelplot()
  m.mainloop()
