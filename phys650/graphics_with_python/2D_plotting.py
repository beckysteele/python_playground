#import packages
import matplotlib.pyplot as plt
import math

#define constants
f0=5.
a0=100.
tdecay=2.

#create lists for the (x,y) data
time = []
amplitude = []

#Calculate the data and append to the lists
for i in range(0, 10000, 1):
	t=0.001 * float(i)
	a = a0 * math.exp(-t/tdecay) * math.cos(2.*math.pi*f0*t)
	time.append(t)
	amplitude.append(a)

#create an x-y plot of the data with labeled axes
plt.figure().canvas.set_window_title('Oscillator')
plt.plot(time, amplitude)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('A Damped Oscillator')

#Show the data
plt.show()
