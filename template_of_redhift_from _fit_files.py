from astropy.io import fits
import numpy as np
from pylab import *
from numpy import *
import os, sys
# code for reading the image 

g_values = fits.open('frame-g-004858-1-0480.fits')
r_values = fits.open('frame-r-004858-1-0480.fits')
u_values = fits.open('frame-u-004858-1-0480.fits')
i_values = fits.open('frame-i-004858-1-0480.fits')
z_values = fits.open('frame-z-004858-1-0480.fits')

g_data = g_values[0].data
r_data = r_values[0].data
u_data = u_values[0].data
i_data = i_values[0].data
z_data = z_values[0].data
print str(g_data.shape[1])
f = open('SDSS_1.train', 'w')
f.write('#zs u g r i z u-g g-r r-i i-z eg er ei ez eu-g eg-r er-i ei-z \n')

#for i in range(0,g_data.shape[0]):
#	for j in range(0,g_data.shape[1]):
for i in range(0,30):
	for j in range(0,30):
			f.write(str(random.randint(0, 10)) + ' ' + str(u_data[i,j]) + ' ' + str(g_data[i,j]) + ' ' + str(r_data[i,j]) + ' ' + str(i_data[i,j]) + ' ' + str(z_data[i,j]) + ' ' + str(u_data[i,j]-g_data[i,j]) + ' ' + str(g_data[i,j]-r_data[i,j]) + ' ' + str(r_data[i,j]-i_data[i,j]) + ' ' + str(i_data[i,j]-z_data[i,j]) + '\n')
f.close()



path_src = os.path.abspath(os.path.join(os.getcwd(), '../../'))
if not path_src in sys.path: sys.path.insert(1, path_src)
from mlz.ml_codes import *

#X and Y can be anything, in this case SDSS mags and colors for X and photo-z for Y
X = loadtxt('SDSS_1.train', usecols=(1, 2, 3, 4, 5, 6, 7), unpack=True).T
Y = loadtxt('SDSS_1.train', unpack=True, usecols=(0,))

#this dictionary is optional for this example
#for plotting the color labels
#(automatically included in MLZ)
d = {'u': {'ind': 0}, 'g': {'ind': 1}, 'r': {'ind': 2}, 'i': {'ind': 3}, 'z': {'ind': 4}, 'u-g': {'ind': 5},
     'g-r': {'ind': 6}}

#Calls the Regression Tree mode
T = TPZ.Rtree(X, Y, minleaf=30, mstar=3, dict_dim=d)
T.plot_tree()
#get a list of all branches
branches = T.leaves()
#print first branch, in this case left ,left, left, etc...
print 'branch = ', branches[0]
#print content of branch
content = T.print_branch(branches[0])
print 'branch content'
print content
#get prediction values for a test data (just an example on how to do it)
#using a train objetc
values = T.get_vals(X[10])
print 'predicted values from tree'
print values
print
print 'mean value from prediction', mean(values)
print 'real value', Y[10]
#Note we use a shallow tree and only one tree for example purposes and there
#is a random subsmaple so answer changes every time
