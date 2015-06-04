import arcpy
import csv

def GetCols(csv):
	""" Get CSV cols so that you can remove duplicate columns in the shapefile using the RemoveCols function """ 
	csvfile = open(csv, "rb")

	cols = csvfile.next().strip().split(",")
	csvfile.close()
	return cols

def RemoveCols(shapefile, cols):
	""" This function removes any specified field from the shapefile if it exists. """

	for col in cols:
		print col
		if arcpy.ListFields(shapefile,col[:10]):
			arcpy.DeleteField_management(shapefile, col)
			print "Field deleted:", col
		else:
			print "No field to delete:", col

def JoinCSV(csvfile, joincolnum, shapefile, shapecolnum):

	""" This function will join a csv file to a shapefile. If there are existing fields with the same name, the field will be removed.
	The joincolnum and shapecolnum refer to the index of the column headers in the file. Column one is 0 due to python syntax."""

	pass

if __name__ == "__main__":
	shapefile = "C:\Mapping_Project\Shapefiles_PostAdd\EUWS2011_CRESTAwJoinCol.shp"
	csv = "C:\Mapping_Project\CSVs\Test.csv"
	allcols = GetCols(csv)
	print allcols
	csvstartcol = 1
	dupcols = []

	for i in range(len(allcols)):
		if i >= csvstartcol:
			dupcols.append(allcols[i]) #custom choose the fields to delete in the shapefile
	print dupcols
	RemoveCols(shapefile, dupcols) 