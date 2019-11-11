## This tool extracts .tgz files taking input parameters of source and destination locations.
## The tool takes in source district code folder name and creates destination folders with
## full district name and extracts data to that location.


## import required modules.
import os
import shutil
from shutil import copyfile
import tarfile
import arcpy
from arcpy import *

## Source_input = raw_input("Browse to source location path of district folder with compressed files: ")
Source_input = arcpy.GetParameterAsText(0)
## Dest_input= raw_input("Browse to the destination location to extract district data: ")
Dest_input = arcpy.GetParameterAsText(1)

## Create a main function with a dictionary for source district code to destination district name.
def main():
    dictDistrict = {}
    dictDistrict = {
    'abl': 'Abilene',
    'ama': 'Amarillo',
    'atl': 'Atlanta',
    'aus': 'Austin',
    'bmt': 'Beaumont',
    'bry': 'Bryan',
    'bwd': 'Brownwood',
    'chs': 'Childress',
    'crp': 'Corpus Christi',
    'dal': 'Dallas',
    'elp': 'El Paso',
    'ftw': 'Fort Worth',
    'hou': 'Houston',
    'lbb': 'Lubbock',
    'lfk': 'Lufkin',
    'lrd': 'Laredo',
    'oda': 'Odessa',
    'par': 'Paris',
    'phr': 'Pharr',
    'sat': 'San Antonio',
    'sjt': 'San Angelo',
    'tyl': 'Tyler',
    'wac': 'Waco',
    'wfs': 'Wichita Falls',
    'ykm': 'Yoakum'}

    ## Using os.walk command, search through source district folders for any .tgz files,
    ## get the parent folder name and create corresponding destination district folder from the dictionary.
    ## Then extract the .tgz files under its respective district folder.

    for root, dirs, files in os.walk(SourceDIR):
        for file in files:
            msg1 = ('File: ' + file)
            print(msg1)
            ##arcpy.AddWarning(msg1)
            
            if (file.endswith("tgz")):
                msg2 = ('Root ' + os.path.basename(root))
                print(msg2)
                arcpy.AddWarning(msg2)
                msg3 = ('file ' + file)
                print(msg3)
                arcpy.AddWarning(msg3)
                
                src_dir = os.path.basename(root)
                fname,fn_ext = os.path.splitext(file)
                src_Tgz_file = os.path.join(SourceDIR,os.path.basename(root),file)
                print ('src_Tgz_file ' + src_Tgz_file)
                dest_dir = dictDistrict[src_dir]
                outPath = os.path.join(DestDir,dest_dir)
                print('outpath '+ outPath)
                print ("Started extracting " + file + " file...")

                tar = tarfile.open(src_Tgz_file, "r:gz")
                tar.extractall(path=outPath, members=None)

                tar.close()
                msg4 = ("Done extracting .tgz files")
                print(msg4)
                arcpy.AddWarning(msg4)

## Calling the main function with input parameters of source and destination locations.                 
if __name__ == "__main__":
    global DestDir
    global SourceDir
    SourceDIR = Source_input
    DestDir = Dest_input
    main()

