import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from astropy.io import fits

# Retrieve catalog from Holwerda et al. (2015)

data = pd.read_csv("holwerda15.csv")
filtered_pairs = data[data["spec_type"] == "PG+ELG"]

# Histogram of redshifts 

# Using this 4-class diverging color scheme that's colorblind safe, print friendly, and photocopy safe: http://colorbrewer2.org/#type=diverging&scheme=PuOr&n=4

z1 = filtered_pairs['z1']
z2 = filtered_pairs['z2']

nbins = 30
binwidth = 0.05

plt.hist(z1, histtype='step', linewidth=3, color='#e66101', bins=np.arange(min(z1), max(z1) + binwidth, binwidth), label='Lensed')
plt.hist(z2, histtype='step', linewidth=3, linestyle='-', color='#5e3c99', bins=np.arange(min(z2), max(z2) + binwidth, binwidth), label='Source')
plt.legend(loc='upper right', numpoints=2)
        
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.ylabel('Galaxy-Galaxy Pairs', fontsize=20)
plt.xlabel(r'Redshift (z)', fontsize=20)

plt.show()