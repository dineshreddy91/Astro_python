from astropy.io import fits
import numpy as np
from pylab import figure, cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

# code for reading the image 
hdulist = fits.open('M86.fits')
scidata = hdulist[0].data
scidata_mean=np.mean(scidata)#mean calculations
scidata_std_deviation=np.std(scidata)#standard deviation calculation
threshold=scidata_mean+scidata_std_deviation
print 'standard_deviation-' + str(scidata_std_deviation)
print 'mean-' + str(scidata_mean)
print 'threshold-' + str(threshold)

#weights calculations for calculating the center of galaxy or star
k,weight_full=(0 for i in range(2))
X,Y,weight=([0 for i in range(10000)] for i in range(3))
for i in range(0,scidata.shape[0]):
	for j in range(0,scidata.shape[1]):
		if scidata[i,j]>threshold:
			weight[k]=scidata[i,j]-threshold
			w=scidata[i,j]-threshold
			weight_full=weight_full+w
			Y[k]=w*i
			X[k]=w*j
			k=k+1
X_center=(sum(X)/weight_full)
Y_center=(sum(Y)/weight_full)
print "X_center-" + str(X_center)
print "Y_center-" + str(Y_center)

#Display the image with log normalization
lm=plt.imshow(scidata, cmap=cm.gray_r, norm=LogNorm(vmin=(scidata_mean+(scidata_std_deviation/2)), vmax=max(weight)))
plt.axis('on')
plt.xlim(X_center-50, X_center+50)
plt.ylim(Y_center-50,Y_center+50)
plt.gray()
plt.show()

