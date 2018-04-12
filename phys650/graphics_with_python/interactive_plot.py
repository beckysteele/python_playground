import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
# and you see in the last line we have added a useful "Slider" control. Next we create a series of time values as a numpy array
f=100.
d=10.
t = np.arange(0, 1, 0.001)
#from 0 to 1 in steps of 0.001 which we take to be seconds. From this we create a matching series of amplitudes

y = np.sin(2*np.pi*t*f)/np.exp(t*d) 
#and a plot

p, = plt.plot(t,y)
#You could stop here with "plt.show()" and be done with simple plot of the sinusoidal function. If you want to add controls to make the plot interactive, then rather than showing the plot now add adjustable subplots. The command

plt.subplots_adjust(bottom=0.25)  
#makes room for the sliders at the bottom of the plot. We add axes

fax = plt.axes([0.25, 0.14, 0.5, 0.03])
#and a frequency Slider

fs = Slider(fax, 'Freq', 0.0, 10.0, valinit=f)
#Now we create a function that updates the frequencies whenever the slider is changed

def f_update(val):
	global f, p
	f = val
	y = np.sin(2*np.pi*t*f)/np.exp(t*d)
	p.set_ydata(y)
	plt.draw();

fs.on_changed(f_update)
#The decay constant slider is the same as this, but for the decay, d, we move it down a bit.

dax = plt.axes([0.25, 0.07, 0.5, 0.03])
ds = Slider(dax, 'Decay', 0.0, 10.0, valinit=d)
def d_update(val):
	global d
	d = val
	y = np.sin(2*np.pi*t*f)/np.exp(t*d)
	p.set_ydata(y)
	plt.draw();

ds.on_changed(d_update)
#Now we show the interactive plot with

plt.show()
