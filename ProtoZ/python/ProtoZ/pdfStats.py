#! /usr/bin/env python

import os
import subprocess
import sys
import tarfile
import datetime
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table


def display_histo(data, mean, median, sigma, outliersPercent, filename):
    """
    """
    # display histogram
    plt.hist(data, bins=100)
    plt.suptitle("Outliers >1.5 Histogram for file: %s" % filename)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    xticks = np.arange(min(data), max(data), 0.25)
    plt.xticks(xticks)
    plt.title('Mean: %2.5f Median: %2.5f Sigma: %2.5f Outliers: %2.5f%% ' % (mean, median, sigma, outliersPercent))
    plt.show()
               
    
#
#-------------------------------------------------------------------------------
#

def file_exist(file):
    """
    """
    if not os.path.exists(file):  
       print '--> Error File not found : ', file
       print '--> Program aborted!'          
       sys.exit()
    
#
#-------------------------------------------------------------------------------
#

def read_table(filename, mode='ascii'):
    """
    """
    print '--> Reading file : ', filename
    data = Table.read(filename, format=mode)
    
    return data
             
#
#-------------------------------------------------------------------------------
#

def compute_stats(array):
    """
    Computes mean, median, sigma and outliers 
    Array contents : sourceIdArr speczArr redshift sedname ebv max
    
    Returns outliers array
    """
    # 
    specZ = array.field(1)
    photZ = array.field(2)

    diffArr = abs(photZ - specZ) 
    plusArr = 1 + specZ  
    dataArr = diffArr / plusArr
    
    mean     = np.average(dataArr)
    median   = np.median(dataArr)
    sigma    = np.std(dataArr)
    outliers = [i for i in dataArr if i >= 0.15]
    outliersPercent =  len(outliers)*100. / len(photZ)
    
    print '--> Mean         : ', mean     
    print '--> Median       : ', median     
    print '--> Sigma        : ', sigma     
    print '--> Outliers     : ', outliersPercent, '%'
    
    return (dataArr, mean, median, sigma, outliersPercent)

#
#-------------------------------------------------------------------------------
#

def main():
    from optparse import OptionParser
    usage = """
            usage: %prog [options] \n           
            
            Compute (from an output file produced by ProtoZpdf which is structured 
            as follows: sourceIdArr speczArr redshift sedname ebv max)
            the standard deviation of [ (photZ - specZ) / 1+specZ ] and
            the outliers fraction as:
                outliers =  (photZ - specZ) / 1+specZ > 0.15  
            and the mean, median and displays an histogram of outliers using
            the option < -d true >           
   
            """ 

    parser = OptionParser(usage, version='%prog version 1.0', description=__doc__)

    parser.add_option("-f", "--file", dest="input_file", type="string",
                      default="/tmp/pdf_catalog.dat",
                      help="Input file to read(catalog) (default: /tmp/pdf_catalog.dat)")
    parser.add_option("-d", "--display", dest="display", type="string",
                      help="Plots the data distribution (by default) ")

    (options, args) = parser.parse_args()
            
    return (options,args)


    
################## MAIN ###########
if __name__ == '__main__':
        
    # Create logger
    

    (options,args) = main()  
    
    # Get program options
    input_file = options.input_file

    file_exist(input_file)
    table = read_table(input_file)    
    (data, mean, median, sigma, outliersPercent) = compute_stats(table)
    if str(options.display) == 'true':
       display_histo(data, mean, median, sigma, outliersPercent, input_file)
    
    
    