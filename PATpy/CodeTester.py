import imp
import arcpy
PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')
shpfile =  "C:\Mapping_Project\Shapefiles\RL13EUWS_PostCresta.shp"
csvfile =  "C:\Mapping_Project\TestPC.csv"
workspace = "C:\Mapping_Project\workspace.gdb"

## first step is to create the directory on the local c drive
#PATpy.CreateDirs()
#PATpy.SetupPerilsEUWS('CRESTA')


# shpcols = PATpy.GetSHPcols(shpfile)
# print shpcols
# csvcols = PATpy.GetCSVcols(csvfile)
# print csvcols


# PATpy.RemoveSHPcols(shpfile, mappingcols)

mappingcols = ['GU_Haz','GU_Vuln','GU_Overall']
# jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"Joincol",shpfile,'JOIN',mappingcols)
# print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'JOIN')

# PATpy.RemoveSHPcols(shpfile, mappingcols)

mxdlist = PATpy.GetMXDList()[1]

lyrs = PATpy.GetLayers(mxdlist)
for lyr in lyrs:
    print lyr
# lyr = 'EUWS2011_CRESTAwJoinCol'

lyr = "RL13EUWS_PostCresta"
PATpy.CreateMapDiffLC(mxdlist,lyr,mappingcols)
