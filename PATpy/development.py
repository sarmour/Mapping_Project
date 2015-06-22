import imp
import arcpy
import os
import sys
import csv
import operator

PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


shpfile =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Zips.shp"
shpfilemaxmin =  "C:\Mapping_Project\Shapefiles\EUFL_RL15_Admin1.shp"
shp_join_col = "JOIN"
shp_join_col2 = "Admin1ID"

##########################JOIN OPTIONS######################################

# cols = PATpy.GetSHPcols(shpfile)

newcols = ['GU_Haz', 'GU_Vuln', 'GU_PLA_Win', 'GU_Overall']

PATpy.AddSHPcols(shpfilemaxmin, newcols, "STRING")

rows = arcpy.SearchCursor(shpfile)
shpvallist = []
joinlist = []
for row in rows:

        vals = {}
        vals["Admin1ID"] = int(row.getValue("Admin1ID"))
        joinlist.append(vals["Admin1ID"])
        for val in newcols:
                vals[val] = float(row.getValue(val))
        shpvallist.append(vals)

joinlist = set(joinlist)
coldict = {}
for col in newcols: #delete the one
        newdict = {}
        for adminval in joinlist:
                vals = []
                for row in shpvallist:
                        if row["Admin1ID"] == adminval:
                                if int(row[col]) == -9999:
                                        vals.append('')
                                else:
                                        vals.append(row[col])
                try:
                        maxval = max(v for v in vals if v <> '')
                except:
                        maxval = "None"
                try:
                        minval = min(vals)
                except:
                        minval = "None"
                maxval = str(int(round(maxval *100,0)))
                minval = str(int(round(minval *100,0)))
                #newdict[adminval] = "Max: " +maxval + "\% Min: "+ minval + "%"
                newdict[adminval] = minval + "\% to "+ maxval + "%"
        coldict[col] = newdict
# print coldict.items()

for col in newcols:
        vals = coldict[col]
        del rows
        rows = arcpy.UpdateCursor(shpfilemaxmin)

        for row in rows:
                shpjoinval = int(row.getValue("Admin1ID"))
                try:
                        row.setValue(str(col),str(vals[shpjoinval]))
                        rows.updateRow(row)
                except:
                    pass




# PATpy.RemoveSHPcols(shpfile, ['ISO3A', 'ISO3N', 'FIPS_1', 'CRESTA'])
# # PATpy.AddSHPcols(shpfile, "JOIN", "STRING")
# PATpy.CalculateField(shpfile, "JOIN", "!RMSCODE! + '_' + str(!POST!)")

# # jointable = PATpy.JoinCSV(csvfile, workspace)
# PATpy.JoinSHP(jointable,"POSTCODE",shpfile,'RMS_CRESTA',mappingcols) #this process can take a while
# print PATpy.CheckMissingSHPVals(csvfile,0, shpfile, 'RMS_CRESTA')


# PATpy.Join_CSV_to_SHP(csvfile, shpfile, shp_join_col, csvjoinindex, csvfieldindex)















# cols = PATpy.GetCSVcols(csvfile)

# PATpy.RemoveSHPcols(shpfile, cols)

# i = 0
# newcols = []
# for col in cols:
#     if i >= csvfieldindex:
#         newcols.append(col)
#     i +=1

# PATpy.AddSHPcols(shpfile, newcols, "double")
# i = 0
# ct = 0
# csvjoinlist = []

# with open(csvfile, 'rb') as csvfile:
#     lib = dict()
#     csvfile.next() #scip the headers
#     for l in csvfile:
#         line = l.rstrip().split(",")
#         csvjoinlist.append(line[csvjoinindex])
#         lib[line[csvjoinindex]] = lib.get(line[csvjoinindex],line[csvfieldindex:])

# rows = arcpy.UpdateCursor(shpfile)
# #rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shp_join_col, method)) ##sorted
# shpjoinlist = []
# missingshpvals = []
# for row in rows:
#     shpjoinval = str(row.getValue(shp_join_col))
#     shpjoinlist.append(shpjoinval)
#     try:
#         vals = lib.get(shpjoinval)
#         for ind, field in enumerate(newcols):
#             row.setValue(str(field),float(vals[ind]))
#             rows.updateRow(row)
#     except:
#         missingshpvals.append(shpjoinval) #This is the shapefile value that there is no corresponding CSV value for. This list is helpful for debugging.
# missingcsvvals = []
# for l in csvjoinlist:
#     if l not in shpjoinlist:
#         missingcsvvals.append(l)

# print missingcsvvals





                        # with open(csvfile, 'rb') as csvfile:
                        #     csvtxt = []
                        #     for l in csvfile:
                        #         csvtxt.append(l.rstrip().split(','))

                        #     for l in csvtxt[1:10]:
                        #         csvjoinval = l[csvjoinindex]
                        #         rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shp_join_col, method))
                        #         for row in rows:
                        #             shpjoinval = str(row.getValue(shp_join_col))
                        #             print csvjoinval, shpjoinval
                        #             break
                        #         break
                        #     for row in rows:
                        #         JOINVAL = str(row.getValue(shp_join_col))
                        #         vals = csvfile.next().rstrip().split(',') #go to next line and parse it to a list
                        #         fieldindex = csvfieldindex
                        #         # print vals[csvjoinindex], JOINVAL
                        #         if str(vals[csvjoinindex]) == JOINVAL:
                        #             print "here 1", vals[csvjoinindex], JOINVAL
                        #             for field in newcols:
                        #                 row.setValue(field,vals[fieldindex])
                        #                 rows.updateRow(row)
                        #                 fieldindex += 1
                        #             ct +=1
                        #         elif JOINVAL in csvjoincols:
                        #             for vals in csvjoinlist:
                        #                 if vals[csvjoinindex] == JOINVAL:
                        #                     print "here 2", vals[csvjoinindex], JOINVAL
                        #                     for field in newcols:
                        #                         row.setValue(field,vals[fieldindex])
                        #                         rows.updateRow(row)
                        #                         fieldindex += 1
                        #                     i +=1
                        #                     csvfile.seek(vals.tell())
                        #                     break



                        # rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shp_join_col, method))
                        # with open(csvfile, 'rb') as csvfile:
                        #     csvjoinlist = []
                        #     csvjoincols = []
                        #     for l in csvfile:
                        #         csvjoinlist.append(l.rstrip().split(','))
                        #         csvjoincols.append(l.rstrip().split(',')[csvjoinindex])
                        #     csvfile.seek(0) #return to start of iterator
                        #     csvfile.next() #skip the headers
                        #     for row in rows:
                        #         JOINVAL = str(row.getValue(shp_join_col))
                        #         vals = csvfile.next().rstrip().split(',') #go to next line and parse it to a list
                        #         fieldindex = csvfieldindex
                        #         # print vals[csvjoinindex], JOINVAL
                        #         if str(vals[csvjoinindex]) == JOINVAL:
                        #             print "here 1", vals[csvjoinindex], JOINVAL
                        #             for field in newcols:
                        #                 row.setValue(field,vals[fieldindex])
                        #                 rows.updateRow(row)
                        #                 fieldindex += 1
                        #             ct +=1
                        #         elif JOINVAL in csvjoincols:
                        #             for vals in csvjoinlist:
                        #                 if vals[csvjoinindex] == JOINVAL:
                        #                     print "here 2", vals[csvjoinindex], JOINVAL
                        #                     for field in newcols:
                        #                         row.setValue(field,vals[fieldindex])
                        #                         rows.updateRow(row)
                        #                         fieldindex += 1
                        #                     i +=1
                        #                     csvfile.seek(vals.tell())
                        #                     break

                        # #############Can i use tell and seek???#######################
                        # #############Can i use set to only get matching vals and improve the process###############



                        #             for l2, line in enumerate(csvfile):
                        #                 if l2 == csvjoinlist[csvjoinindex].index(JOINVAL):
                        #                     print JOINVAL, line
                        #                     break
                        #             i +=1

                        #             for l in f:
                        #                 print l
                        #                 vals = l.split(',')
                        #                 fieldindex = csvfieldindex
                        #                 if vals[csvjoinindex] == JOINVAL:
                        #                     for field in newcols:
                        #                         row.setValue(field,vals[fieldindex])
                        #                         rows.updateRow(row)
                        #                         fieldindex += 1
                        #                         print "here"
                        #             del f



                        # line = csv.readline()
                        # print line
                        # line = csv.readline()
                        # print line
                        # csv.close()
                        # for row in rows:
                        #     JOINVAL = row.getValue(shp_join_col)
                        #     fieldindex = csvfieldindex

                        #     if
                        #     for line in csv:
                        #         vals = line.strip().split(",")
                        #         if vals [csvjoinindex] == JOINVAL:
                        #             for field in newcols:
                        #                 row.setValue(field,vals[fieldindex])
                        #                 rows.updateRow(row)
                        #                 fieldindex += 1
                        #         # if rows.next().getValue() == line.next().strip().split(",")[csvjoinindex]:
                        #         # print row.getValue(shp_join_col)
                        #         # print rows.next().getValue(shp_join_col)
                        #         # print csv.next().strip().split(",")[csvjoinindex]
                        #         # print csv.next().strip().split(",")[csvjoinindex]
                        #         # print row.getValue(shp_join_col)
                        #         # print kill

                        #             print dir(rows)
                        #             print dir(csv)
                        #             print killa8l
                        #                     # vals = csv.next().strip().split(",")
                        #         # print vals
                        #         # if vals [csvjoinindex] == JOINVAL:
                        #         #         # print vals[csvjoinindex], JOINVAL
                        #         #         for field in newcols:
                        #         #             row.setValue(field,vals[fieldindex])
                        #         #             rows.updateRow(row)
                        #         #             fieldindex += 1



                        # # # newlst = []

                        # # # for row in rows:
                        # # #     vals = []
                        # # #     for field in fields:
                        # # #         vals.append(row.getValue(field.name))
                        # # #     newlst.append(vals)

                        # # # for l in newlst[:10]:
                        # # #     print l
