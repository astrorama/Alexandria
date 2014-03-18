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
        redshiftedSed.add_row((row[0]*(1+z),row[1]))
    return redshiftedSed

if __name__ == '__main__':

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
    args = parser.parse_args()
    
    options = None
    if args.conf:
        options = elConf.parse_conf_file(args.conf)
    else:
        options = elConf.parse_conf_file(elConf.find_conf_file('ProtoZ', 'ProtoZflux'))
    filterPath = options['filter-dir-path'][0]
    sedPath = options['sed-dir-path'][0]
    redLawPath = options['red-law-dir-path'][0]
    
    sedMap = chdm.get_seds(sedPath)
    sed = sedMap[args.sed]
    
    redLawMap = chdm.get_reddening_curves(redLawPath)
    if args.redLaw:
        redLaw = redLawMap[args.redLaw]
    else:
        redLaw = redLawMap['calzetti']
        
    ebv = 0.
    if args.ebv:
        ebv = args.ebv
    
    if ebv != 0:
        reddenedSed = _reddenSed(sed, redLaw, ebv)
    else:
        reddenedSed = sed
    
    fig, axes = plt.subplots(nrows=len(args.zlist), ncols=1)
    for i in range(len(args.zlist)):
        z = args.zlist[i]
        redshiftedSed = _redshiftSed(reddenedSed, z)
        filterAxes = axes[i]
        filterAxes.set_title(args.sed + ' at Z=' + str(z))
        phzPlt.plot_all_filters(filterAxes, filterPath)
        for line in filterAxes.lines:
            if line.get_color() == 'k':
                line.set_color('r')
            maxX = 0
            maxY = 0
            for x,y in line.get_xydata():
                if y > maxY:
                    maxX = x
                    maxY = y
            filterAxes.text(maxX, maxY, line.get_label()[0], fontsize=20, color=line.get_color())
        filterAxes.set_xlabel('Wavelength [Ang]')
        filterAxes.set_ylabel('Transmission')
        xlim = filterAxes.get_xlim()
        sedAxes = filterAxes.twinx()
        phzPlt.plot_2d_table(sedAxes,'SED',redshiftedSed)
        sedAxes.lines[0].set_color('k')
        sedAxes.set_ylabel(u'F\u03bb')
        sedAxes.set_xlim(xlim)
    fig.subplots_adjust(hspace=.4)
    plt.show(block=True)