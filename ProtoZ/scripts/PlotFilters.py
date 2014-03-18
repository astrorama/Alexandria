#! /usr/bin/env python

import os.path
import matplotlib.pyplot as plt
import ProtoZ.ElementsConf as elConf
import ProtoZ.PHZPlot as phzPlt

if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser(description="""
        Plots the PHZ filters in one plot. The filters are located according the
        parameters (only one should be given). If no parameter is given the default
        configuration file of the ProtoZflux executable is used.
        """)
    parser.add_argument("-d", "--dir", help=
        "The path to the directory containing the filters", metavar='FILE')
    parser.add_argument("-c", "--conf", help=
        'An elements configuration file containing the "filter-dir-path" parameter', metavar='FILE')
    args = parser.parse_args()

    dir = args.dir
    conf = args.conf
    
    path = None
    if dir:
        path = dir
    else:
        options = None
        if conf:
            options = elConf.parse_conf_file(conf)
        else:
            options = elConf.parse_conf_file(elConf.find_conf_file('ProtoZ', 'ProtoZflux'))
        if options and options.has_key('filter-dir-path'):
            path = options['filter-dir-path'][0]
    if not path:
        print 'No filter directory found'
        exit()
    if not os.path.isdir(path):
        print path + ' is not a directory'
        exit()
        
    fig, axes = plt.subplots()
    phzPlt.plot_all_filters(axes, path)
    axes.legend()
    axes.set_xlabel('Wavelength [Ang]')
    axes.set_ylabel(u'F\u03bb')
    plt.show(block=True)