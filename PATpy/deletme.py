# mxds = 'test.mxd'
# mapfields = 'test.mxd'
# print mxds
# print mapfields
# if type(mxds) is str:
#     newmxd = []
#     newmxd.append(mxds)
#     mxds = newmxd
# if type(mapfields) is str:
#     newmapfields = []
#     newmapfields.append(mapfields)
#     mapfields = newmapfields
# print mxds
# print mapfields

import sys
import csv
import operator
import os
import arcpy

shpfile =  "C:\Mapping_Project\Shapefiles\EUWS2011_CRESTAwJoinCol - copy.shp"

sort_field = "RMS_CRESTA"
method = "D"
L = []
vals = []
# i = 0
# for field in arcpy.ListFields(shpfile):
#     rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (sort_field, method))
#     for row in rows:
#         # print field.name, row.getValue(field.name)
#         vals.append(row.getValue(field.name))
#     if i == 0:
#         L = vals
#     else:
#         L = zip(L,vals)
#     i +=1
# print L
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
newlist =  zip (a,b)
print "".join(newlist)
