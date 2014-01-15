#! /usr/bin/env python
#""" 
#   arg :  
#
#   The script does the following:
#   
#   
#   Date: 10-September-2013 Version 1.0 Author: NM 
#         - Creation
#"""   


import os
import glob
import sys
import datetime
import logging
import pprint
import numpy as np
import pylab as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
from collections import Counter

diskStorage = '/Users/admin/Euclid/comparison_faros_lephare/' # Disk storage (e.g. where to put log file)
logFile     = 'magnitude_comparaison.log'  # Log file
lephareResultFile = diskStorage + 'filter_sed_magnitude_lephare_results_file.txt'

#title            ='Magnitude Comparison Faros-Lephare : with LINEAR Interpolation, NO GALLEX filters'
#faros_file       = diskStorage + 'magnitude_all_seds_all_filters_LINEAR_WITHOUT_GALLEX.txt'

#title            ='Magnitude Comparison Faros-Lephare : with Cubic-Spline Interpolation, NO GALLEX filters'
#faros_file       = diskStorage + 'magnitude_all_seds_all_filters_CUBIC_WITHOUT_GALLEX.txt'

title            ='Magnitude Comparison Faros-Lephare : with Cubic-Spline Interpolation'
faros_file       = diskStorage + 'magnitude_all_seds_all_filters_CUBIC.txt'
diffFile         = diskStorage + 'filter_sed_magnitude_diff_file_CUBIC.txt'

#title            ='Magnitude Comparison Faros-Lephare : with Linear Interpolation'
#faros_file       = diskStorage + 'magnitude_all_seds_all_filters_LINEAR.txt'
#diffFile         = diskStorage + 'filter_sed_magnitude_diff_file_LINEAR.txt'

mag_lephare_file = diskStorage + 'GAL_FAROS.dat'
sed_lephare_list = diskStorage + 'COSMOS_MOD.list'

#
#-------------------------------------------------------------------------------
#

def set_logger(logFileName):
    """
    This function creates logger with 'spam_application'
    
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    if not os.path.exists(diskStorage):
        fh = logging.FileHandler(logFileName)
    else:
        logPath = diskStorage+"/"
        if not os.path.exists(logPath):
            try:               
                os.makedirs(logPath)
            except os.error:
                    print logPath + logFileName
                    print os.errno
                    print os.strerror
        fh = logging.FileHandler(logPath+logFileName)

    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

#
#-------------------------------------------------------------------------------
#

def read_faros_file():
    """
    Contents of the Faros file:
       SED name   , Filter name , Magnitude  , z_step
       element[0] , element[1]  , element[2] , element[3]
    """
    print '--> Reading Faros file   : ', faros_file
    mag_faros_arr = []  
    if os.path.exists(faros_file) : 
       file = open(faros_file,'r')                       
       for line in file:
           element = line.split()
           if not element[0] == '#': 
               mag_faros_arr.append([ element[0], element[1], element[2], element[3] ])          
       file.close()
    else:
        log.error("File not found %s", faros_file)
            
    return mag_faros_arr


def read_lephare_files():
    """
    Read the ascii file for the "magnitude" produced by lephare at all
    redshift and result is stored into an arrays as follows:
    [ SED name, FILTER name, Magnitude , Redshift]
    """
    
    print '--> Reading lephare file : ', lephareResultFile
    
    lephareFile = open(lephareResultFile,'w')
    
    # Read the SED list
    sed_lephare_arr = []
    if os.path.exists(sed_lephare_list) : 
        file = open(sed_lephare_list,'r')
        for line in file:
            line = line.replace("COSMOS_SED/","")
            line = line.replace(".sed","")
            sed_lephare_arr.append(line)           
    else:
        log.error("File not found %s", sed_lephare_list)
        sys.exit()
        
    # Read the lephare magnitude file
    mag_lephare_arr = [] 
    if os.path.exists(mag_lephare_file) : 
       file = open(mag_lephare_file,'r')  
       for line in file:
           element = line.split()
           # Comment line with filter names
           if element[0] == '#': 
               line_with_filter = line.split()
               #print line
           else:
               filter_index = element[0]    
               # Store all magnitudes for each filter
               index = 3
               # Decode each line
               while index < len(line_with_filter):
                   sed          = sed_lephare_arr[int(element[0])-1]
                   sed          = sed.replace('\n','')
                   z_step       = element[4]
                   mag          = element[9+index-3]
                   filter       = line_with_filter[index] 
                   mag_lephare_arr.append([ sed, filter, mag , z_step])
                   #print  'Lephare --> SED: ', sed,' filter: ',  filter,' Mag: ', mag ,' z_step:', z_step
                   lephareFile.write('SED : ' + sed + ' filter : ' + filter +' Magnitude : ' + str(mag) + ' z_step : ' + z_step + '\n')
                   index += 1
       lephareFile.close()
       file.close()
    else:
       log.error("File not found %s", mag_lephare_file)
       sys.exit()
         
    return (mag_lephare_arr)



#
#-------------------------------------------------------------------------------
#

def compare_data(faros_data, lephare_data):
    """
    Compute magnitude differences. Result is an array as follows:
    [SED, FILTER, difference_value]
    
    """
    print '--> Compare magnitudes'
    diff_file = open(diffFile,'w') 
    
    diff_arr = []
    # Loop on faros data
    for faros in faros_data:
        sed_faros    = faros[0] 
        filter_faros = faros[1] 
        mag_faros    = faros[2] 
        z_faros      = faros[3]
        # look for the same data in lephare
        for lephare in lephare_data:
            sed_lephare    = lephare[0] 
            filter_lephare = lephare[1] 
            mag_lephare    = lephare[2] 
            z_lephare      = lephare[3]
            #print sed_faros,' ', filter_faros,' ',mag_faros,' ', float(z_faros)
            #print sed_lephare,' ', filter_lephare,' ',mag_lephare,' ', float(z_lephare)
            if sed_lephare == sed_faros and filter_lephare == filter_faros and float(z_lephare) == float(z_faros):
                #print 'compare: ',sed_lephare,' ', filter_lephare,' ',mag_lephare,' z_lephare: ', z_lephare, ' z_faros: ',z_faros
                diff_mag = float(mag_faros) - float(mag_lephare)
                diff_arr.append([sed_faros, filter_faros, float(diff_mag), z_faros ])
                #print sed_faros,' ', filter_faros,' ',mag_faros, ' diff_mag: ',diff_mag, ' z_step: ',z_faros
                # Store in a file all mag_diff too big
                #if (diff_mag >= 0.01):
                #    diff_file.write( 'SED : ' + sed_faros + ' Filter : ' + filter_faros + ' Magnitude Lephare : ' + str(mag_lephare) + ' Magnitude Faros : ' + str(mag_faros) + ' diff_mag: ' + str(diff_mag) +'\n')
                redshift = "%.2f" % float(z_faros)
                diff_file.write( 'SED : ' + sed_faros + ' Filter : ' + filter_faros + ' Magnitude Lephare : ' + str(mag_lephare) + ' Magnitude Faros : ' + str(mag_faros) + ' diff_mag: ' + str(diff_mag) + ' z_step: ' + redshift + '\n')
                continue
    
    diff_file.close()
        
    return np.array(diff_arr)

   
# Return a column i of the matrix         
def display_histograms(data, filter_names, num_filter, sed_names, num_sed):
    """
    Display histograms
    """
    i=j=1
    # Number of z steps
    num_zstep = len(data)/(num_sed*num_filter)
    numColdisplay = len(data)/num_zstep
    colors = iter(cm.rainbow(np.linspace(0, 1, numColdisplay)))


    # Number of graphs in function of redshift
    num_graphs = num_zstep

    # Preprare arrays for histograms
    x = []
    for step in data[:,3]: 
        x.append(np.double( data[:,2][data[:,3]== step ]))
                
    redshift = data[:,3] 
    
    xArr = np.array(x)  
    min_val = xArr.min()
    max_val = xArr.max()
    
    plt.figure()
    for i in range(num_graphs): 
        print '--> Number of graphs : ', num_graphs
        fig = plt.subplot(num_graphs, 1, i+1)   
        plt.subplots_adjust(hspace = .8)                    
        # Normalize histogram
        plt.hist([xArr[i]], bins=100,  histtype='bar', range=(min_val,max_val),color=next(colors))        
        #plt.hist([xArr[i]], bins=100,  histtype='bar', color=next(colors))        
        plt.ylabel('z = ' + redshift[i])
        max_xticks = 10
        max_yticks = 2
        xloc = plt.MaxNLocator(max_xticks)
        fig.xaxis.set_major_locator(xloc)
        yloc = plt.MaxNLocator(max_yticks)
        fig.yaxis.set_major_locator(yloc)
        i += 1
        fig.yaxis.set_label_position("right")

    plt.xlabel('Difference lephare-faros ' ) 
    plt.suptitle('Faros-Lephare Magnitude difference at several redshifts, SED# : '+ str(num_sed) +' Filter#: ' + str(num_filter))
    if num_filter == 1 :   
        plt.suptitle('Faros-Lephare Magnitude difference at several redshifts, SED# : '+ str(num_sed) +' Filter: ' + str(filter_names[0]))
    if num_sed == 1:
        plt.suptitle('Faros-Lephare Magnitude difference at several redshifts, SED : '+ str(sed_names[0]) +' Filter#: ' + str(num_filter))
    
    print 'Total values per histogram : ',  len(data[:,2][data[:,3]=='0.00' ]) 
    plt.show()        


def get_sedfilter_info(diff_mag, redshift):
    """
    The selection is based on redshift 0.00
    """
    
    # Number of SEDs
    #print diff_mag
    #print diff_mag[:,0][diff_mag[:,3]==redshift ]
    num_sed = len(diff_mag[:,0][diff_mag[:,3]==redshift ])
    sed_names = diff_mag[:,0][diff_mag[:,3]==redshift ]
        
    # Exctract all filters
    one_line_arr = diff_mag[:,1][diff_mag[:,3]==redshift ] 

    # Count the number of filters
    filters = Counter(one_line_arr)
        
    # Extract filter names
    filter_names = []
    num_filter   = len(filters)

    for num in range(num_filter):
        filter_names.append(one_line_arr[num])

    return (filter_names, num_filter, sed_names, num_sed)
 
 
               
def main():

    from optparse import OptionParser
    usage = """
            usage: %prog [options] arg \n           
            
            The script reads data(3 files) produced by Faros and Lephare about
            the magnitude for all SEDs through all Filters and makes an 
            histogram of the differences of the results.                        
 
            """ 

    parser = OptionParser(usage, version='%prog version 1.0', description=__doc__)

#    parser.add_option("-d", "--data_type", dest="data_type", type="string",
#                     default="scw",
#                      help="Data type to be backed up, tm or scw (default: scw)")

#    parser.add_option("-e", "--last_rev", dest="last_revolution", type="int",
#                      help="Last revolution to be backed up, e.g. 1200")    

    (options, args) = parser.parse_args()
       
    # Make sure rev is given
#   if len(args) != 1:
#       log.info("")
#       log.error("Script aborted! Revolution number is missing!!!  \n")
#       parser.print_help() 
#       exit(-1) 

    # Check arg is a number
#   if not sys.argv[1].isdigit():
#       log.error("")
#       log.error("Revolution number is not a number: %s !!!" % sys.argv[1])
#       log.error("Script aborted!")
#       sys.exit()

    return (options,args)


    
################## MAIN ###########
if __name__ == '__main__':
        
    # Create logger
    set_logger(logFile)
    log = logging.getLogger()

    (options,args) = main()  
        
    log.info('')
    log.info('Script started at: %s ' % datetime.datetime.today())
    
    # Get Lephare information 
    lephare_data = read_lephare_files()
    
    # Get Faros information 
    faros_data   = read_faros_file()

    diff_mag = compare_data(faros_data, lephare_data)
    
    #print diff_mag
    
    # Select in function of redshift
    redshift = '0.00'    
    (filter_names, num_filter, sed_names, num_sed ) = get_sedfilter_info(diff_mag, redshift)
    
    print '--> Number of filter(s) :', num_filter
    print '--> Filter names:'
    print filter_names
    print '--> Number of SED(s)    : ', num_sed
    print '--> SED names :'
    print  sed_names
    
    # Display histogram           
    display_histograms(diff_mag, filter_names, num_filter, sed_names, num_sed)

    log.info('')
    log.info('Log file         : %s ', diskStorage+logFile)
    log.info('')

    log.info('')
    log.info('Script ended at: %s ' % datetime.datetime.today())
        
