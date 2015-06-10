import imp
import arcpy
PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')



workspace = "C:\Mapping_Project\workspace.gdb"

shpfile =  "C:\Mapping_Project\Shapefiles\RL13EUWS_PostCresta.shp"
csvfile =  "C:\Mapping_Project\TestPC.csv"

# shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol.shp"
# csvfile =  "C:\Mapping_Project\TestCRESTA.csv"

## first step is to create the directory on the local c drive
#PATpy.CreateDirs()
#PATpy.SetupPerilsEUWS('CRESTA')


# csvcols = PATpy.GetCSVcols(csvfile)
# print csvcols




mappingcols = ['GU_Haz','GU_Vuln','GU_Overall']
# PATpy.RemoveSHPcols(shpfile, mappingcols)

# # PATpy.RemoveSHPcols(shpfile, mappingcols)
# # shpcols = PATpy.GetSHPcols(shpfile)
# # print shpcols

# jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"Joincol",shpfile,'JOIN',mappingcols) #this process can take a while
# print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'JOIN')



mxdlist = PATpy.GetMXDList()[1]
print mxdlist

# # lyrs = PATpy.GetLayers(mxdlist)
# # for lyr in lyrs:
# #     print lyr
# # lyr = 'EUWS2011_CRESTAwJoinCol'

lyr = "RL13EUWS_PostCresta"
PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Diff_LC")
# #PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Percent_Change")
