import imp
import arcpy
import os
PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


### Set Up Workspace ###

# PATpy.CreateDirs()
# workspace = PATpy.CreateWorkspace()
# PATpy.SetupPerilsEUWS('CRESTA')
# PATpy.SetupPerilsEUFL('POST')
# SetupPerilsEUWS('POST')

# #########################Set up variables################################
# workspace = "C:\Mapping_Project\workspace.gdb"
shpfile =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Zips.shp"
shpfile1 =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_RiverZips.shp"
shp_join_col = "JOIN"

csvfile =  "C:\Mapping_Project\TestPC.csv"
csvjoinindex = 0
csvfieldindex = 1


##########################JOIN OPTIONS######################################

csvcols = PATpy.GetCSVcols(csvfile)
print csvcols

mappingcols = ['GU_Haz', 'GU_Overall']
shpcols = PATpy.GetSHPcols(shpfile)
print shpcols
# PATpy.RemoveSHPcols(shpfile, ['ISO3A', 'ISO3N', 'FIPS_1', 'CRESTA'])
# # PATpy.AddSHPcols(shpfile, "JOIN", "STRING")
# PATpy.CalculateField(shpfile, "JOIN", "!RMSCODE! + '_' + str(!POST!)")

# # jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"POSTCODE",shpfile,'RMS_CRESTA',mappingcols) #this process can take a while
# print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'RMS_CRESTA')


# PATpy.Join_CSV_to_SHP(csvfile, shpfile, shp_join_col, csvjoinindex, csvfieldindex)


# missingresults2 = PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'JOIN')

# print missingresults2


mxdlist = PATpy.GetMXDList()
print mxdlist
EUmxds = ['C:\\Mapping_Project\\MXDs\\EUFL_Postcode.mxd']
Othermxds = ['C:\\Mapping_Project\\MXDs\\EUFL_Postcode_Belgium.mxd']

# # PATpy.GetLayers(mxdlist)

# lyr = os.path.basename(shpfile).strip(".shp")
# print lyr

# # ##PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Diff_LC")
# PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Percent_Change")

#
PATpy.CreateMaps2(EUmxds,shpfile, shpfile1, mappingcols,"Percent_Change")

PATpy.CreateMaps2(Othermxds,shpfile, shpfile1, mappingcols,"Percent_Change", False, True)



