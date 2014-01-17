#! /usr/bin/env python
# Author NM

import os
import subprocess
import sys
import tarfile
import datetime
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table



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
 

    diffArr = photZ - specZ
    plusArr = 1 + specZ  
    dataArr = diffArr / plusArr
    
    mean     = np.average(dataArr)
    median   = np.median(dataArr)
    sigma    = np.std(dataArr)
    
    # Mean absolute deviation
    mad = np.median(abs(dataArr - median)) 
    
    absDataArr = abs(dataArr)
    outliers = [i for i in absDataArr if i > 0.15]
    outliersPercent =  len(outliers)*100. / len(photZ)
 
    # Without outliers
    noOutliersArr   = [i for i in absDataArr if i <= 0.15]
    sigmaNoOutliers = np.std(noOutliersArr)
    meanNoOutliers  = np.average(noOutliersArr)
    
                    
    print '--> Mean                : ', mean     
    print '--> Median              : ', median     
    print '--> Sigma               : ', sigma     
    print '--> Mad                 : ', mad     
    print '--> Outliers            : ', outliersPercent, '%'
    print '--> Sigma (no outliers) : ', sigmaNoOutliers     
   
    return (specZ, photZ, dataArr, mean, median, sigma, mad, outliersPercent, sigmaNoOutliers, meanNoOutliers)

#
#-------------------------------------------------------------------------------
#

def display_data(specZ, photZ, data, mean, median, sigma, mad, outliersPercent, sigmaNoOutliers, meanNoOutliers, filename):
    """
    """
    # First plot specZ/photZ
    
    fig1 = plt.subplot(2, 1, 1, aspect=1.0)  # 2 graphs 
    plt.subplots_adjust(hspace = .4) 
                       
    plt.xlabel("SpecZ")
    plt.ylabel("PhotZ")
    plt.plot(np.arange(0, max(photZ)),np.arange(0, max(photZ)),"r")
    plt.plot(specZ,photZ,"yo")
    plt.plot(plt.xlim(), plt.xlim(),"r")
        
    fig2 = plt.subplot(2, 1, 2)  # 2 graphs 
    plt.subplots_adjust(hspace = .4)
   
    # Second plot (histogram)
    
    barValues, bins, patches = plt.hist(data, bins=100) 

    plt.axvline(x=0.15,color='r')
    plt.axvline(x=-0.15,color='r')
    plt.suptitle("Outliers >1.5 Histogram for file: %s" % filename)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title('Distribution of : (photZ - specZ)/(1 + specZ)')
              
    # Write information
    txt = ' Mean : %2.5f\n Median : %2.5f\n Mad : %2.5f\n Sigma : %2.5f\n Outliers : %2.5f%%\n Sigma(no outliers) : %2.5f\n Mean((no outliers) : %2.5f ' \
        % (mean, median, mad, sigma, outliersPercent, sigmaNoOutliers, meanNoOutliers)
    plt.text(max(bins)-0.5, max(barValues), txt, fontsize=15, family='sans-serif', style='italic', ha='left', va='top')
    
    plt.show() 
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
    parser.add_option("-n", "--noplot", dest="display", action="store_false",
                      default=True,
                      help="Plots the data distribution (by default) ")

    (options, args) = parser.parse_args()
            
    return (options,args)


    
################## MAIN ###########
if __name__ == '__main__':
            
    (options,args) = main()  
    
    # Get program options
    input_file = options.input_file   
    file_exist(input_file)
    # Read file
    table = read_table(input_file)
    # Get stats    
    (specZ, photZ, data, mean, median, mad, sigma, outliersPercent,sigmaNoOutliers, meanNoOutliers) = compute_stats(table)
    # Plot distribution
    if options.display:
       display_data(specZ, photZ, data, mean, median, mad, sigma, outliersPercent, sigmaNoOutliers, meanNoOutliers, input_file)
    
    
    