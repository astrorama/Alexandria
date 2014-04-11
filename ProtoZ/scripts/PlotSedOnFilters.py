#! /usr/bin/env python

import ProtoZ.ElementsConf as elConf
import ProtoZ.ChDataModel as chdm
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import ProtoZ.PHZPlot as phzPlt

def _reddenSed(sed, redLaw, ebv):
    redLawValues = np.interp(sed[sed.colnames[0]],redLaw[redLaw.colnames[0]],redLaw[redLaw.colnames[1]])
    reddenedSed = Table(names=['Wavelength','Flux'])
    for i in range(len(sed)):
        newValue = sed[i][1]*pow(10.,-0.4*redLawValues[i]*ebv)
        reddenedSed.add_row((sed[i][0],newValue))
    return reddenedSed

def _redshiftSed(sed, z):
    redshiftedSed = Table(names=['Wavelength','Flux'])
    for row in sed:
        redshiftedSed.add_row((row[0]*(1+z),row[1]/((1+z)**2)))
    return redshiftedSed

def _multiplySedWithFilter(sed, filter):
    filterValues = np.interp(sed[sed.colnames[0]],filter[filter.colnames[0]],filter[filter.colnames[1]], left=0, right=0)
    filteredSed = Table(names=['Wavelength','Flux'])
    for i in range(len(sed)):
        newValue = sed[i][1]*filterValues[i]
        filteredSed.add_row((sed[i][0],newValue))
    return filteredSed

if __name__ == '__main__':

    # Set the command line parameters
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Plots a given SED above the filters.')
    parser.add_argument("-s", "--sed", help=
        'The name of the SED to plot', metavar='FILE')
    parser.add_argument("-z", "--zlist", nargs='+', type=float, help=
        'A list of redshifts to plot', default=[0.], metavar='FILE')
    parser.add_argument("-c", "--conf", help=
        'An ProtoZflux configuration file', metavar='FILE')
    parser.add_argument("-r", "--redLaw", help=
        'The reddening curve to use for reddening (default "calzetti"', metavar='FILE')
    parser.add_argument("-e", "--ebv", type=float, help=
        'The E(B-V) value to use for reddening', metavar='FILE')
    parser.add_argument("-f", "--fillFilter", help='''The name of the filter to fill 
        its area multiplied with the SED or "all" for all filters''', metavar='NAME')
    parser.add_argument("-g", "--sedGray", nargs=2, type=float, help=
        'A range in wavelength in which the restframe SED values will be filled with gray')
    args = parser.parse_args()
    
    # Get from the configuration file all the information we need
    options = None
    if args.conf:
        options = elConf.parse_conf_file(args.conf)
    else:
        options = elConf.parse_conf_file(elConf.find_conf_file('ProtoZ', 'ProtoZflux'))
    filterPath = options['filter-dir-path'][0]
    sedPath = options['sed-dir-path'][0]
    redLawPath = options['red-law-dir-path'][0]
    
    # Retrieve the filters data
    filterMap = chdm.get_filters(filterPath)
    
    # Retrieve the table containing the SED data
    sedMap = chdm.get_seds(sedPath)
    sed = sedMap[args.sed]
    
    # Retrieve the table containing the reddening curve data
    redLawMap = chdm.get_reddening_curves(redLawPath)
    if args.redLaw:
        redLaw = redLawMap[args.redLaw]
    else:
        redLaw = redLawMap['calzetti']
    
    ebv = 0.
    if args.ebv:
        ebv = args.ebv
    
    # Do the reddening of the SED
    if ebv != 0:
        reddenedSed = _reddenSed(sed, redLaw, ebv)
    else:
        reddenedSed = sed
    
    # Create one plot for each Z value
    fig, axes = plt.subplots(nrows=len(args.zlist), ncols=1)
    sed_y_max = 0
    for i in range(len(args.zlist)):
        # Redshift the SED
        z = args.zlist[i]
        redshiftedSed = _redshiftSed(reddenedSed, z)
        
        #Plot all the filters
        filterAxes = axes[i]
        phzPlt.plot_all_filters(filterAxes, filterPath)
        xlim = filterAxes.get_xlim()
        
        for line in filterAxes.lines:
            # We don't want to have black lines for filters. SED will be black.
            if line.get_color() == 'k':
                line.set_color('r')
            # We add a text with the filter name on its maximum value
            maxX = 0
            maxY = 0
            for x,y in line.get_xydata():
                if y > maxY:
                    maxX = x
                    maxY = y
            filterAxes.text(maxX, maxY, line.get_label()[0], fontsize=16, color=line.get_color())
            
        # Fix the filters Y axis scale
        filterAxes.set_ylim(0, 1)
        filterAxes.set_ylabel('Transmission')
        # Add the title on top left corner
        filterAxes.text(0.01, 0.9, args.sed + ' at Z=' + str(z), ha='left', fontsize=13, transform=filterAxes.transAxes)
        # Remove the labels of the X axis (only the last plot should have them)
        plt.setp(filterAxes.get_xticklabels(), visible=False)
        
        # Create a new axes to plot the SED as a twin of the filterAxes
        sedAxes = filterAxes.twinx()
        phzPlt.plot_2d_table(sedAxes,'SED',redshiftedSed)
        sedAxes.lines[0].set_color('k')
        sedAxes.lines[0].set_linewidth(2)
        sedAxes.set_ylabel(u'F\u03bb')
        
        # Fill the area of the SED multiplied by each filter
        if args.fillFilter:
            for line in filterAxes.lines:
                if args.fillFilter == 'all' or line.get_label() == args.fillFilter:
                    if args.fillFilter == 'all':
                        color = line.get_color()
                    else:
                        color = 'k'
                    filteredSed = _multiplySedWithFilter(redshiftedSed, filterMap[line.get_label()])
                    phzPlt.fill_2d_table(sedAxes, '', filteredSed)
                    sedAxes.collections[-1].set_color(color)
                    sedAxes.collections[-1].set_alpha(0.3)
        
        # Fill the area under the SED
        if args.sedGray:
            min = 0
            max = 0
            for i in range(len(sed)):
                if sed[i][0] < args.sedGray[0]:
                    min = i
                if sed[i][0] < args.sedGray[1]:
                    max = i
            phzPlt.fill_2d_table(sedAxes, '', redshiftedSed[min:max])
            sedAxes.collections[-1].set_color('k')
            sedAxes.collections[-1].set_alpha(0.3)
        
        # Set the SED axis to cover only the filters
        sedAxes.set_xlim(xlim)
        if sed_y_max < sedAxes.get_ylim()[1] :
            sed_y_max = sedAxes.get_ylim()[1]
        sedAxes.set_ylim(0, sed_y_max)
    
    # Add the X axis labels only for the last plot
    axes[-1].set_xlabel('Wavelength [Ang]')
    plt.setp(axes[-1].get_xticklabels(), visible=True)
    fig.subplots_adjust(hspace=.05)
    plt.show(block=True)