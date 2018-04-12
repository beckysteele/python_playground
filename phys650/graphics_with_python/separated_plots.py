# Import the plotting and math packages
import matplotlib.pyplot as plt
import math
# Define initial constants
f0 = 5.
tdecay = 2.
# Create lists for the (x,y) data
time = []
sine_amplitude = []
exp_amplitude = []
product_amplitude = []
# Calculate the data and append to the lists
for i in range(0, 10000, 1):
  t = 0.001 * float(i) 
  a1 = math.cos(2. * math.pi * f0 * t)
  a2 = math.exp(-t/tdecay)
  a = a1*a2
  time.append(t)
  sine_amplitude.append(a1)
  exp_amplitude.append(a2)
  product_amplitude.append(a)
# Create an x-y plot with labels
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('A Damped Oscillator')
plt.plot(time,exp_amplitude,'r.', label='Exponential')
plt.plot(time, product_amplitude,'b-', label='Sine', linewidth=1.5)
plt.legend()
# Show the data
plt.show()
