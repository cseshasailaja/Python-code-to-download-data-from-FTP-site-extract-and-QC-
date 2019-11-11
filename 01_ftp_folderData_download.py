##Script tool to download data from FTP site to Network drive.

##import required modules
import ftplib
from ftplib import FTP
import os
import sys
import tarfile
import zipfile
import arcpy
from arcpy import *

## 1.
## For IP address of source FTP Host Server, go to https://dnschecker.org/
## Enter FTP site url, to get IP address


server = arcpy.GetParameterAsText(0)
##username = raw_input("Enter your Username: ")
username = arcpy.GetParameterAsText(1)
##password = raw_input("Enter your Password: ")
password = arcpy.GetParameterAsText(2)

## 2.
## Accessing FTP Host Server, source location, and select local/network destination path...

ftp = ftplib.FTP(server)
ftp.login(username, password)
msg1 = "FTP Host Server login success..."
print(msg1)
arcpy.AddWarning(msg1)

##source = raw_input("Copy path to FTP source lacation: ")
source = arcpy.GetParameterAsText(3)

## destination = raw_input("Browse to local/network destinaion folder: ")
destination = arcpy.GetParameterAsText(4)

## 3.
## Function to download a single file from FTP to local...

def grabFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    msg2 = "Download complete"
    print(msg2)
    arcpy.AddWarning(msg2)
    localfile.close()
    
## 4.
## Change working directory to FTP source and create a list of source district folders/files as an array.

ftp.cwd(source)
folderFileList=ftp.nlst()

## 5.
## Loops through each distict folder from the source list and creates a district folder if not exists
## in the destination path.
## Check for folders excluding . and .. folders. 

for folder in folderFileList:
    if len(folder) > 2:
        sourceFolderPath = source + r"/" + folder
        print(sourceFolderPath)

        os.chdir(destination)
        destinationFolderPath = destination + r"/" + folder
        if not os.path.exists(folder):
            os.mkdir(folder)
            msg3 = "created destination folder: " + destinationFolderPath
            print(msg3)
            arcpy.AddWarning(msg3)
            
            ## Change the working directory to source district folder to get a list of files that
            ## needs to be downloded.
            ## Loop through the list of folders and download each file by calling the function that you
            ## created to download a single file.

            ftp.cwd(sourceFolderPath)
            sourceFileList = ftp.nlst()
            for sourceFile in sourceFileList:
                ftp.cwd(sourceFolderPath)
                if sourceFile.endswith(".tgz"):
                    msg4 = sourceFile
                    print(msg4)
                    arcpy.AddWarning(msg4)

                    os.chdir(destinationFolderPath)
                    destinationFile = sourceFile
                    grabFile(destinationFile)
                    
    ## If the FTP source has only files and no folders, then loop through each file in the folder/files list and call the function to download single file.

    else:
        for file in folderFileList:
            ftp.cwd(source)
            if file.endswith(".tgz"):
                msg5 = file
                print(msg5)
                arcpy.AddWarning(msg5)

                os.chdir(destination)
                destinationFile = file
                grabFile(destinationFile)

## ---END---

    

        
        



