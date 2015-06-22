
import imp, arcpy

PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


shpfile =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Zips.shp"
shp_join_col = "JOIN"

shpfilemaxmin =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Admin1.shp"
shp_join_col2 = "Admin1ID"

csvfile =  "C:\Mapping_Project\TestPC_2.csv"
csvjoinindex = 0
csvfieldindex = 1

# cols = PATpy.GetCSVcols(csvfile)
# print cols

difflccols = ['LC_Haz', 'LC_Vuln', 'LC_PLA_Wind', 'LC_Overall']
perchangecols = ['PC_Haz', 'PC_Vuln', 'PC_PLA_Wind', 'PC_Overall']

# PATpy.Join_CSV_to_SHP(csvfile, shpfile, shp_join_col, csvjoinindex, csvfieldindex)

# PATpy.JoinSHPspecialEUFL(shpfile, shp_join_col, shpfilemaxmin, shp_join_col2, perchangecols)

# print PATpy.CheckMissingSHPVals(csvfile, csvjoinindex, shpfile, shp_join_col)

# mappingfiles = PATpy.GetMXDList()

# EUmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_Europe.mxd'
# PATpy.CreateMaps(EUmxd, shpfile, difflccols, "Diff_LC")

CNTRYmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_Belgium.mxd'
PATpy.CreateMaps(EUmxd, shpfile, difflccols, "Diff_LC")

# subCNTRYmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_SubBelgium.mxd'
