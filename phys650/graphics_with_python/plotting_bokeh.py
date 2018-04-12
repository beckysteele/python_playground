from bokeh.plotting import figure, output_file, show
import math as m
#and in this case also Python math. For more advanced work, you might use numpy and scipy or other packages as well, but here we are only going to plot something simple.

#Next, create or import the data you want to plot. You need two lists, one for "x" and one for "y" starting like this

npoints = 1000
x = []
y = []
f1 = 100.
f2 = 80.
a1 = 5.
a2 = 5.
#which created empty lists of x and y, and defined some variables we will use to fill those lists with data, in this case the sum of two sine functions. Generate the lists point by point

for i in range(npoints):
	t = float(i)/10000.
	arg1 = 2.*m.pi*f1*t
	arg2 = 2.*m.pi*f2*t
	amplitude = a1*m.sin(arg1) + a2* m.sin(arg2)
	x.append(t)
	y.append(amplitude)
#by appending values for each x and y. Lastly, give a file name that you want the program to use to store the output, create the graphics, and show the result.

output_file("sines.html")
p = figure()
p.line(x, y, line_width=2)
show(p)
exit()
