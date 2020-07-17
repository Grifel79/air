#!/usr/bin/python

#----------------------------------------------------#
#  getFileFromUrlList.py                             # 
#  Jim Hofman                                            #
#  Saves files from a list of urls                   #
#                                                                 #
#----------------------------------------------------#

# Revisions
# 8-18-2014 - added switch to direct downloaded files  to a specific directory
#                  - added usage() method

from urllib.request import urlretrieve
from os import path, getcwd
import sys, getopt
from time import time
import requests
from requests.auth import HTTPDigestAuth

# Returns a file from the url and saves it as 'fname'
def save_file_from_url(local_url, dir): 
    # split the url and get the last element in the list (the file name)
    fname = local_url.split('/')[-1] 
    print("Downloading: " + local_url)
    try:

        #urlretrieve(local_url, dir+fname.strip(), reporthook)

        username = 'Grifel79'
        password = 'Grifopt79!'

        r = requests.get(local_url, auth=HTTPDigestAuth(username, password))
        open(dir+fname.strip(), 'wb').write(r.content)


    except Exception as e:
        print('Error downloading %s: error: %s' % (local_url, e))

def reporthook(count, block_size, total_size):
   global start_time
   if count == 0:          # first pass, initialize the time
      start_time = time()
      return
   duration = time() - start_time
   size     = int(count * block_size)
   speed    = int(size / (1024 * duration))
   percent  = min(int(count * block_size * 100 / total_size),100)
   sys.stdout.write("\r...%d%% @ %d KBytes/second, Download time: %d  seconds" % \
               (percent, speed, duration))
   sys.stdout.flush()        
  
       
def usage():
   print('There are only 2 options: ')
   print('       -o <dir> or --output <dir> to specify a path to an output directory in which to store the downloaded files.')
   print('           NOTE:  the output directory must exist.  If no directory is specified, the files will be donwloaded ')
   print('           to the directory in which the script is running.')
   print('      -h to display this message ')
 
 
def main(argv):


   # Declarations
   # output_dir - specifies directory in which to store the file (default - directory in which the script is run.
    output_dir = ''
    # file_list is a list or all the urls from which we will retrieve a file
    file_list =["https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2019/oco2_LtCO2_191231_B9003r_200130003035s.nc4","https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200101_B9003r_200204190325s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200102_B9003r_200204190440s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200103_B9003r_200204190754s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200108_B9003r_200204190946s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200109_B9003r_200204191010s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200110_B9003r_200204191136s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200111_B9003r_200204191415s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200112_B9003r_200204191626s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200113_B9003r_200204191752s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200114_B9003r_200204192011s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200115_B9003r_200204192230s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200116_B9003r_200204192449s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200117_B9003r_200204192650s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200118_B9003r_200204192849s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200119_B9003r_200204193103s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200120_B9003r_200204193223s.nc4",
"https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_FP.9r/2020/oco2_LtCO2_200121_B9003r_200204193452s.nc4"]

    try:
        opts, args = getopt.getopt(argv,'ho:', ['output='])
    except:
        print("Exception getting arguments.")
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-o', '--output'):
            output_dir = arg
            print('Output directdory is %s' % output_dir)
        else:
            pass

    for url in file_list:
        try:
            save_file_from_url(url, output_dir)
        except Exception as e:
            print('Could not save file from: %s' % url)
    print('\nDone')

if __name__ == "__main__":
    main(sys.argv[1:])
