import imp
import arcpy
import os
PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


#### Set Up Workspace ###

#PATpy.CreateDirs()
#workspace = PATpy.CreateWorkspace()
# PATpy.SetupPerilsEUWS('CRESTA')
# PATpy.SetupPerilsEUFL('POST')
#SetupPerilsEUWS('POST')

# # #########################
# workspace = "C:\Mapping_Project\workspace.gdb"
# shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol.shp"
# csvfile =  "C:\Mapping_Project\TestCRESTA.csv"

# # csvcols = PATpy.GetCSVcols(csvfile)
# # print csvcols

# mappingcols = ['Haz','Vuln','Overall']

# shpcols = PATpy.GetSHPcols(shpfile)

# print shpcols

# jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"POSTCODE",shpfile,'RMS_CRESTA',mappingcols) #this process can take a while
# print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'RMS_CRESTA')



# mxdlist = PATpy.GetMXDList()[0]
# print mxdlist

# # PATpy.GetLayers(mxdlist)

# lyr = os.path.basename(shpfile).strip(".shp")
# print lyr

# # ##PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Diff_LC")
# PATpy.CreateMaps(mxdlist,lyr,mappingcols,"Percent_Change")



csvjoinindex = 0
csvfieldindex = 1
cols = PATpy.GetCSVcols(csvfile)
i = 0
newcols = []
for col in cols:
    if i >= csvfieldindex:
        newcols.append(col)
    i +=1

PATpy.AddSHPcols(shpfile, newcols, "double")


rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shp_join_col, method))

for row in rows:
    JOINVAL = row.getValue(shp_join_col)
    fieldindex = csvfieldindex

    with open(csvfile, 'rb') as csv:
        try:
            vals = csv.strip().split(",").next()
            print vals
            if vals [csvjoinindex] == JOINVAL:
                    print vals[csvjoinindex], JOINVAL
                    for field in newcols:
                        row.setValue(field,vals[fieldindex])
                        rows.updateRow(row)
                        fieldindex += 1
        except:
            print "here"
            for line in csv:
                vals = line.strip().split(",")
                if vals [csvjoinindex] == JOINVAL:
                    # print vals[csvjoinindex], JOINVAL
                    for field in newcols:
                        row.setValue(field,vals[fieldindex])
                        rows.updateRow(row)
                        fieldindex += 1
                    break



