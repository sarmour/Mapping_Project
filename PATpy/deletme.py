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

csvfile =  "C:\Mapping_Project\TestPC.csv"
reader = csv.reader(open(csvfile), delimiter=",")
i = 0
for l in reader:
    i +=1
    if i <10 :
        print l
    else:
        break
sortedlist = sorted(reader, key=operator.itemgetter(0))

# with open(csvfile) as csvfile:
#     for l in csvfile:
#         print l
for l in sortedlist[:10]:
    print l

