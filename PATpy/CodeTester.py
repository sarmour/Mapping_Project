import imp
import arcpy
import os
PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


#### Set Up Workspace ###

# Patpy.CreateDirs()
# workspace = Patpy.CreateWorkspace
# Patpy.SetupPerilsEUWS('CRESTA')
#SetupPerilsEUWS('POST')

#########################
workspace = "C:\Mapping_Project\workspace.gdb"
shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol.shp"
csvfile =  "C:\Mapping_Project\TestCRESTA.csv"

# shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol.shp"
# csvfile =  "C:\Mapping_Project\TestCRESTA.csv"

# csvcols = PATpy.GetCSVcols(csvfile)
# print csvcols

mappingcols = ['Haz','Vuln','Overall']

# shpcols = PATpy.GetSHPcols(shpfile)
# print shpcols

# jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"POSTCODE",shpfile,'RMS_CRESTA',mappingcols) #this process can take a while
#print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'RMS_CRESTA')



mxdlist = PATpy.GetMXDList()[0]
print mxdlist

PATpy.GetLayers(mxdlist)

lyr = os.path.basename(shpfile).strip(".shp")
# print lyr

##PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Diff_LC")
PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Percent_Change")
