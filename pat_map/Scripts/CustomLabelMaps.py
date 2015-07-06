
import imp, arcpy

PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


shpfile =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Zips.shp"
shp_join_col = "JOIN"
shpsubregioncode = 'CNY_CRESTA'

shpfilemaxmin =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Admin1.shp"
aggregationcol = "Admin1ID"

csvfile =  "C:\Mapping_Project\TestPC_2.csv"
csvjoinindex = 0
csvfieldindex = 1

# cols = PATpy.GetCSVcols(csvfile)
# print cols

difflccols = ['LC_Haz', 'LC_Vuln', 'LC_PLA_Wind', 'LC_Overall']
perchangecols = ['PC_Haz', 'PC_Vuln', 'PC_PLA_Wind', 'PC_Overall']
labelcols = []
for l in perchangecols:
    labelcols.append("L_"+l[:8])

# PATpy.Join_CSV_to_SHP(csvfile, shpfile, shp_join_col, csvjoinindex, csvfieldindex)

# PATpy.JoinSHPspecialEUFL(shpfile, shp_join_col, shpfilemaxmin, aggregationcol, perchangecols)

# print PATpy.CheckMissingSHPVals(csvfile, csvjoinindex, shpfile, shp_join_col)

# CalcPerChangeSHP(shpfile, shp_join_col, aggregationcol, precentchangecols)

# mappingfiles = PATpy.GetMXDList()

# EUmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_Europe.mxd'
# PATpy.CreateMaps(EUmxd, shpfile, difflccols, "Diff_LC", False)

# CNTRYmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_Belgium.mxd'
# PATpy.CreateMaps3(CNTRYmxd, shpfile, difflccols, labelcols,"Diff_LC")

subCNTRYmxd = 'C:\\Mapping_Project\\MXDs\\EUFL_PC_SubBelgium.mxd'

# labels = PATpy.CalcPerChangeSHP(shpfile, shpjoincol, shpsubregioncode, perchangecols)
# labels = ['L_PC_Haz', 'L_PC_Vuln', 'L_PC_PLA_W', 'L_PC_Overa']

PATpy.CreateMaps3(subCNTRYmxd,shpfile, difflccols, labels, "diff_lc")

