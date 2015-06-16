import imp
import arcpy
import os
import sys
import csv
import operator

PATpy = imp.load_source('PATpy', 'C:\Mapping_Project\PATpy\JoinFunctions.py')


shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol - copy.shp"
csvfile =  "C:\Mapping_Project\TestCRESTA.csv"
shp_join_col = "RMS_CRESTA"
method = "A"
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
i = 0
ct = 0
csvjoinlist = []

with open(csvfile, 'rb') as csvfile:
    lib = dict()
    csvfile.next() #scip the headers
    for l in csvfile:
        line = l.rstrip().split(",")
        csvjoinlist.append(line[csvjoinindex])
        lib[line[csvjoinindex]] = lib.get(line[csvjoinindex],line[csvfieldindex:])

rows = arcpy.UpdateCursor(shpfile)
#rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shp_join_col, method)) ##sorted
shpjoinlist = []
missingshpvals = []
for row in rows:
    shpjoinval = str(row.getValue(shp_join_col))
    shpjoinlist.append(shpjoinval)
    try:
        vals = lib.get(shpjoinval)
        for ind, field in enumerate(newcols):
            row.setValue(str(field),float(vals[ind]))
            rows.updateRow(row)
    except:
        missingshpvals.append(shpjoinval) #This is the shapefile value that there is no corresponding CSV value for. This list is helpful for debugging.
missingcsvvals = []
for l in csvjoinlist:
    if l not in shpjoinlist:
        missingcsvvals.append(l)

print "Missed shp values ".join(missingshpvals)
print "Missing csv values ".join(missingcsvvals)





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
    # for row in rows:
    #     JOINVAL = str(row.getValue(shp_join_col))
    #     vals = csvfile.next().rstrip().split(',') #go to next line and parse it to a list
    #     fieldindex = csvfieldindex
    #     # print vals[csvjoinindex], JOINVAL
    #     if str(vals[csvjoinindex]) == JOINVAL:
    #         print "here 1", vals[csvjoinindex], JOINVAL
    #         for field in newcols:
    #             row.setValue(field,vals[fieldindex])
    #             rows.updateRow(row)
    #             fieldindex += 1
    #         ct +=1
    #     elif JOINVAL in csvjoincols:
    #         for vals in csvjoinlist:
    #             if vals[csvjoinindex] == JOINVAL:
    #                 print "here 2", vals[csvjoinindex], JOINVAL
    #                 for field in newcols:
    #                     row.setValue(field,vals[fieldindex])
    #                     rows.updateRow(row)
    #                     fieldindex += 1
    #                 i +=1
    #                 csvfile.seek(vals.tell())
    #                 break



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

##############Can i use tell and seek???#######################
##############Can i use set to only get matching vals and improve the process###############



            # for l2, line in enumerate(csvfile):
            #     if l2 == csvjoinlist[csvjoinindex].index(JOINVAL):
            #         print JOINVAL, line
            #         break
            # i +=1

            # for l in f:
            #     print l
            #     vals = l.split(',')
            #     fieldindex = csvfieldindex
            #     if vals[csvjoinindex] == JOINVAL:
            #         for field in newcols:
            #             row.setValue(field,vals[fieldindex])
            #             rows.updateRow(row)
            #             fieldindex += 1
            #             print "here"
            # del f



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
