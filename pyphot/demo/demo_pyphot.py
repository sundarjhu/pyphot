import pyphot #synthetic photometry
from astropy.table import Table #synthetic photometry
import numpy as np #input/output
from astropy.io import fits #input/output
from matplotlib import pyplot as plt #visualisation
pkgdir = '/usr/local/lib/python2.7/site-packages/pyphot/' #Edit this depending on user
libsdir = '/usr/local/lib/python2.7/site-packages/pyphot/libs/' #Edit this depending on user
demodir = '/Users/sundar/work/pyphot/pyphot/demo/' #Edit this depending on user

"""Load entire HDF5 library"""
libraryName=pkgdir+'libs/synphot_PhIReSSTARTer.hd5'
filterLibrary = pyphot.get_library(fname=libraryName)

"""Names of the first ten filters available in the library"""
filterNames = filterLibrary.get_library_content()
for i in range(9):
        print filterNames[i]

"""Load information for a single filter"""
ans_3300 = filterLibrary.load_filters(['ans_3300']) #result is a list, even for a single filter!
"""Load information for a list of filters"""
filters = filterLibrary.load_filters(['ans_3300', 'steward_k'])

"""View filter information"""
ans_3300[0].info()

"""We will use the same set of filters for both examples below"""
filterNames = ['MCPS_U', 'MCPS_B', 'MCPS_U', 'MCPS_I', '2MASS_J', '2MASS_H', '2MASS_Ks',
                                  'SPITZER_IRAC_36', 'SPITZER_IRAC_45', 'SPITZER_IRAC_58', 'SPITZER_IRAC_80',
                                  'SPITZER_MIPS_24']
libraryName = libsdir+'synphot_PhIReSSTARTer.hd5'
filterLibrary = pyphot.get_library(fname=libraryName)

#Input spectrum
spec = np.loadtxt(demodir+'IRC+10216_ISO_SWS.dat', comments='#', usecols=(0,1))
#Retrieve filter responses interpolated over input wavelength grid
filterList = filterLibrary.load_filters(filterNames, interp=True, lamb=spec[:,0]*pyphot.unit['micron'])

#Upon execution, cls contains the central wavelengths for each filter, and sed the
#   synthetic photometry in that filter.
cls, sed = pyphot.extractPhotometry(spec[:,0], spec[:,1], filterList, Fnu=True, absFlux=False)
lamCen = np.array([a.magnitude for a in cls])

#Plot results
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(spec[:,0], spec[:,1], '--', label='ISO SWS spectrum')
ax.plot(lamCen, sed, 'o', color='red', label='Synthetic photometry')
ax.set_xlabel('Wavelength (micron)')
ax.set_ylabel('Flux (Jy)', rotation=90.)
for i in range(len(filterNames)):
        ax.text(lamCen[i], sed[i]*1.2, filterNames[i], horizontalalignment='center', verticalalignment='bottom', fontsize=8, rotation=90.)
        plt.title('Example 1: IRC+10216')
        plt.show()

"""Read in the GRAMS C-star grid"""
"""IGNORE WARNINGS"""
hdulist = fits.open(demodir+'grams_c.fits')
cg = hdulist[1].data
hdulist.close()
inlam = cg['LSPEC'][0] #input wavelength in micron
infnu = cg['FSPEC'] #input flux grid in Jy
#Retrieve filter responses interpolated over input wavelength grid
filterList = filterLibrary.load_filters(filterNames, interp=True, lamb=inlam*pyphot.unit['micron'])

#Upon execution, cls contains the central wavelengths for each filter, and seds the
#   synthetic photometry for each input spectrum in that filter.
cls, seds = pyphot.extractSEDs(inlam, infnu, filterList, Fnu=True, absFlux=False)
lamCen = np.array([a.magnitude for a in cls])

#Plot results
f, axarr = plt.subplots(2, 2)
specnum = [0, 99, 10345, 3000]
ct=0
for i in range(2):
        for j in range(2):
            axarr[i,j].plot(inlam, infnu[specnum[ct],:], '--', label='GRAMS model spectrum #'+str(specnum[ct]+1))
            axarr[i,j].plot(lamCen, seds[specnum[ct],:], 'o', color='red', label='Synthetic photometry')
            if i==1:
                axarr[i,j].set_xlabel('Wavelength (micron)')
            if j==0:
                axarr[i,j].set_ylabel('Flux (Jy)', rotation=90.)
            #for k in range(len(filterNames)):
            #    axarr[i,j].text(lamCen[k], seds[specnum[i+j],k]/40, filterNames[k], 
            #            horizontalalignment='left', verticalalignment='bottom', 
            #                    fontsize=8, rotation=90.)
            axarr[i,j].set_xscale('log')
            axarr[i,j].set_yscale('log')
            axarr[i,j].set_title('Model spectrum #'+str(specnum[ct]+1), fontsize=10)
            ct = ct + 1
plt.setp([a.get_xticklabels() for a in axarr[0,:]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:,1]], visible=False)
plt.suptitle('Example 2: the GRAMS carbon-star grid', fontsize=12)
plt.show()
