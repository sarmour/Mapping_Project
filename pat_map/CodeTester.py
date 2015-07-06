import imp
import arcpy
import os
pat_map = imp.load_source('pat_map', 'C:\Mapping_Project\pat_map\JoinFunctions.py')


### Set Up Workspace ###

# pat_map.CreateDirs()
# workspace = pat_map.CreateWorkspace()
# pat_map.SetupPerilsEUWS('CRESTA')
# pat_map.SetupPerilsEUFL('POST')
# SetupPerilsEUWS('POST')

# #########################Set up variables################################
# workspace = "C:\Mapping_Project\workspace.gdb"
shpfile =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Zips.shp"
shpjoincol = "JOIN"

csvfile =  "C:\Mapping_Project\TestPC.csv"
csvjoinindex = 0
csvfieldindex = 1

difflccols = ['LC_Haz', 'LC_Vuln', 'LC_PLA_Wind', 'LC_Overall']
perchangecols = ['PC_Haz', 'PC_Vuln', 'PC_PLA_Wind', 'PC_Overall']

##########################JOIN OPTIONS######################################

SHPcols = pat_map.GetSHPcols(shpfile)
print SHPcols


# pat_map.AddSHPcols(shpfile, "CNY_CRESTA", "STRING")
field = "CNY_CRESTA"

# pat_map.CalculateField(shpfile, field, "!FIPS! + '_' + str(!ZONE1!)")


# mappingcols = ['GU_Haz', 'GU_Overall']
# shpcols = pat_map.GetSHPcols(shpfile)
# print shpcols
# # pat_map.RemoveSHPcols(shpfile, ['ISO3A', 'ISO3N', 'FIPS_1', 'CRESTA'])
# # # pat_map.AddSHPcols(shpfile, "JOIN", "STRING")
# # pat_map.CalculateField(shpfile, "JOIN", "!RMSCODE! + '_' + str(!POST!)")

# # # jointable = pat_map.JoinCSV(csvfile, workspace)
# # pat_map.JoinSHP(jointable,"POSTCODE",shpfile,'RMS_CRESTA',mappingcols) #this process can take a while
# # print pat_map.CheckMissingSHPVals(csvfile,0, shpfile, 'RMS_CRESTA')


# # pat_map.Join_CSV_to_SHP(csvfile, shpfile, shpjoincol, csvjoinindex, csvfieldindex)


# # missingresults2 = pat_map.CheckMissingSHPVals(csvfile,0, shpfile, 'JOIN')

# # print missingresults2


# mxdlist = pat_map.GetMXDList()
# print mxdlist
# EUmxds = ['C:\\Mapping_Project\\MXDs\\EUFL_Postcode.mxd']
# CNTRYmxds = ['C:\\Mapping_Project\\MXDs\\EUFL_Postcode_Belgium.mxd']

# # # pat_map.GetLayers(mxdlist)

# # lyr = os.path.basename(shpfile).strip(".shp")
# # print lyr

# # # ##pat_map.CreateMaps(mxdlist,lyr,mappingcols,"Diff_LC")
# # pat_map.CreateMaps(mxdlist,lyr,mappingcols,"Percent_Change")

# #
# pat_map.CreateMaps2(EUmxds,shpfile, shpfile1, mappingcols,"Percent_Change")

# pat_map.CreateMaps2(CNTRYmxds,shpfile, shpfile1, mappingcols,"Percent_Change", False, True)

subCNTRYmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_CRESTAs.mxd'
shpsubregioncode = 'CNY_CRESTA'

labels = pat_map.CalcPerChangeSHP(shpfile, shpjoincol, shpsubregioncode, perchangecols)
# labels = ['L_PC_Haz', 'L_PC_Vuln', 'L_PC_PLA_W', 'L_PC_Overa']

pat_map.CreateMaps3(subCNTRYmxd,shpfile, difflccols, labels, "diff_lc")

