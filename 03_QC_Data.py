## This tool checks the data by opening shapefiles, csv and dbf tables in a folder and
## feature classes and geodatabase tables in a file geodatabase by giving record counts in each file.
## Confirming the file is good and not corrupted if it gives record counts of the underlying tables.

import arcpy
from arcpy import *
import os
import sys

## ws = r"C:\...\02_extract"
## ws = raw_input("Browse to the location of Data folder: ")
ws = arcpy.GetParameterAsText(0)
for (path, dirs, files) in os.walk(ws):
    errorCount = 0
    for dir in dirs:
        if dir.endswith(".gdb"):
            gdbPath = os.path.join(path, dir)
            msg0 = gdbPath
            print(msg0)
            arcpy.AddWarning(msg0)

            arcpy.env.workspace = gdbPath

            ## List feature classes in the geodatabase and get record counts of each feature class.
            
            fcList = arcpy.ListFeatureClasses()
            try:
                for fc in fcList:
                    fcRecCnt = arcpy.GetCount_management(fc)
                    msg1 = " " + fc + ": record count = " + str(fcRecCnt)
                    print(msg1)
                    arcpy.AddWarning(msg1)
            except:
                e = sys.exc_info()[1]
                msgE = (e.args[0])
                print(msgE)
                arcpy.AddWarning(msgE)
                errorCount =+ 1

            ## List tables in the geodatabase and get record counts of each table.

            tblList = arcpy.ListTables()
            try:
                for tbl in tblList:                     
                    tblRecCnt = arcpy.GetCount_management(tbl)
                    msg2 = " " + tbl + ": record count = " + str(tblRecCnt)
                    print(msg2)
                    arcpy.AddWarning(msg2)
            except:
                e = sys.exc_info()[1]
                msgE = (e.args[0])
                print(msgE)
                arcpy.AddWarning(msgE)
                errorCount =+ 1

            ## List datasets in the geodatabase and then list feature classes in each dataset and get
            ## record count of each feature class.
                
            datasets = arcpy.ListDatasets()

            for dataset in datasets:
                featureclasses = arcpy.ListFeatureClasses(feature_dataset = dataset)

                try:
                    for featureclass in featureclasses:                       
                        fcRecordCount = arcpy.GetCount_management(featureclass)
                        msg3 = " " + dataset + ": " + featureclass + " - record count = " + str(fcRecordCount)
                        print(msg3)
                        arcpy.AddWarning(msg3)

                except:
                    e = sys.exc_info()[1]
                    msgE = (e.args[0])
                    print(msgE)
                    arcpy.AddWarning(msgE)
                    errorCount =+ 1

            ## List geodatabase tables in each dataset and get record count of geodatabase table.

            for dataset in datasets:
                tables = arcpy.ListTables()

                try:
                    for table in tables:                                                   
                        tableRecordCount = arcpy.GetCount_management(table)
                        msg4 = " " + dataset + ": " + table + " - record count = " + str(tableRecordCount)
                        print(msg4)
                        arcpy.AddWarning(msg4)

                except:
                    e = sys.exc_info()[1]
                    msgE = (e.args[0])
                    print(msgE)
                    arcpy.AddWarning(msgE)
                    errorCount =+ 1
                    
    ## If the dir is a folder with .shp, .csv and .dbf files...
        
    for f in files:
        if f.endswith(".shp"):            
            filePath = os.path.join(path)
            msg5 = filePath
            print(msg5)
            arcpy.AddWarning(msg5)
            shpRecordCount = arcpy.GetCount_management(f)
            msg6 = " " + f + ": record count = " + str(shpRecordCount)
            print(msg6)
            arcpy.AddWarning(msg6)
        elif f.endswith(".dbf"):
            dbfRecordCount = arcpy.GetCount_management(f)
            msg7 = " " + f + ": record count = " + str(dbfRecordCount)
            print(msg7)
            arcpy.AddWarning(msg7)
        elif f.endswith(".csv"):
            csvRecordCount = arcpy.GetCount_management(f)
            msg8 = " " + f + ": record count = " + str(csvRecordCount)
            print(msg8)
            arcpy.AddWarning(msg8)


            

if errorCount == 0:
    msg9 = "All files passed QC"
    print(msg9)
    arcpy.AddWarning(msg9)
                    

                        
                        
                    


