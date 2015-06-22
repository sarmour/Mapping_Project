#Embedded file name: C:/Mapping_Project\Scripts\ShapefileCodes.py
###Developed by Shane Armour###

import os
from numpy import genfromtxt, loadtxt
import arcpy
from shutil import copy
from glob import glob
import shutil
import operator

def CreateDirs():
    """Creates a folder directory on the C drive called Mapping_Project. Following this function, run the movePeril() function to create a local copy of MXDs and shapefiles."""
    try:
        if not os.path.exists("C:\Mapping_Project"):
            os.mkdir("C:\Mapping_Project")

        if not os.path.exists("C:\Mapping_Project\MXDs"):
            os.mkdir("C:\Mapping_Project\MXDs")

        if not os.path.exists("C:\Mapping_Project\Shapefiles"):
            os.mkdir("C:\Mapping_Project\Shapefiles")

        if not os.path.exists("C:\Mapping_Project\Out"):
            os.mkdir("C:\Mapping_Project\Out")
    except:
        print "There was an error creating the directories."

def CreateWorkspace():
    """ This function will check if a .gbp workspace exists. If there is not one, the script will make one. This script returns the path of the workspace. The .gbp workspace is useful for working with csv data"""
    path = 'C:\\Mapping_Project\\workspace.gdb'
    if not os.path.exists('C:\\Mapping_Project\\workspace.gdb'):
        arcpy.CreateFileGDB_management('C:\\Mapping_Project\\', 'workspace.gdb')
    else:
        print 'you already have a workspace there'
    return  path

def SetupSymb():
    """This function creates local copies of symbology. """
    destsymbdir = "C:\Mapping_Project\MXDs\Symbology"
    if not os.path.exists("C:\Mapping_Project\MXDs\Symbology"):
        os.mkdir("C:\Mapping_Project\MXDs\Symbology")
    if not os.path.exists("C:\Mapping_Project\MXDs\Symbology\PercentChange.lyr"):
        for fl in glob(r"\\ca1ntap01\grm\PAT\ArcMappingTool\Symbology\PercentChange\\*"):
            shutil.copy2(fl,destsymbdir)
def SetupPerilsEUWS(maptype):
    """ Moves the RMS MXD template and shapefiles from the GRM drive to the local drive. MXD location is hardcoded. Maptype options = 'CRESTA' or 'POST'"""
    destmxddir = "C:\Mapping_Project\MXDs"
    destSHPdir = "C:\Mapping_Project\Shapefiles"

    SetupSymb()
    if maptype == 'CRESTA':
        try:
            shutil.copy2(r"\\ca1ntap01\grm\PAT\ArcMappingTool\MXDs\EUWS\EUWS_CRESTA.mxd",destmxddir)
        except:
            if os.path.exists("C:\Mapping_Project\MXDs\EUWS_CRESTA.mxd") :
                    print "The EUWS map already exists on your local machine."
            else:
                print "Error with SetupPerilsEUWS"

        for fl in glob(r"\\ca1ntap01\grm\PAT\ArcMappingTool\Shapefiles\EUWS_CRESTA\*"):
            try:
                shutil.copy2(fl,destSHPdir)
            except:
                print "Was not able to copy over ", os.path.basename(fl)
    if maptype == 'POST':
        try:
            shutil.copy2(r"\\ca1ntap01\grm\PAT\ArcMappingTool\MXDs\EUWS\EUWS_Postcode.mxd",destmxddir)
        except:
            if os.path.exists("C:\Mapping_Project\MXDs\EUWS_Postcode.mxd") :
                    print "The EUWS map already exists on your local machine."
            else:
                print "Error with SetupPerilsEUWS"

        for fl in glob(r"\\ca1ntap01\grm\PAT\ArcMappingTool\Shapefiles\EUWS_Postcode\*"):
            try:
                shutil.copy2(fl,destSHPdir)
            except:
                print "Was not able to copy over ", os.path.basename(fl)

def SetupPerilsEUFL(maptype):
    """ Moves the RMS MXD template and shapefiles from the GRM drive to the local drive. MXD location is hardcoded. Maptype options = 'CRESTA' or 'POST'"""
    destmxddir = "C:\Mapping_Project\MXDs"
    destSHPdir = "C:\Mapping_Project\Shapefiles"

    SetupSymb()
    if maptype == 'CRESTA':
        try:
            shutil.copy2(r"\\ca1ntap01\grm\PAT\ArcMappingTool\MXDs\EUFL\EUFL_CRESTA.mxd",destmxddir)
        except:
            if os.path.exists("C:\Mapping_Project\MXDs\EUFL_CRESTA.mxd") :
                    print "The EUFL map already exists on your local machine."
            else:
                print "Error with SetupPerilsEUFL"

        for fl in glob(r"\\ca1ntap01\grm\PAT\ArcMappingTool\Shapefiles\EUFL_CRESTA\*"):
            try:
                shutil.copy2(fl,destSHPdir)
            except:
                print "Was not able to copy over ", os.path.basename(fl)
    if maptype == 'POST':
        try:
            shutil.copy2(r"\\ca1ntap01\grm\PAT\ArcMappingTool\MXDs\EUFL\EUFL_Postcode.mxd",destmxddir)
        except:
            if os.path.exists("C:\Mapping_Project\MXDs\EUFL_Postcode.mxd") :
                    print "The EUFL map already exists on your local machine."
            else:
                print "Error with SetupPerilsEUFL"

        for fl in glob(r"\\ca1ntap01\grm\PAT\ArcMappingTool\Shapefiles\EUFL_Postcode\*"):
            try:
                shutil.copy2(fl,destSHPdir)
            except:
                print "Was not able to copy over ", os.path.basename(fl)



def GetCSVcols(csvfile):
    """ Returns a list of the CSV headers."""
    with open(csvfile, 'rb') as csv:
        cols = csv.next().strip().split(',')
    return cols

def ReadCSV(csvfile):
    """ This function will print the lines in an unformatted csv. To join the csv, please use the JoinCSV function."""
    with open(csvfile) as csv:
        for l in csv:
            print l

def SortCSV(csvfile, colindex = 0, reverse = False):
    """ This script will sort a csv based on the colindex and csvfile path. If reverse is True, the values will be sorted in reverse index. This function assumes that the csv has headers. colindex starts at 0"""
    data = []
    with open(csvfile,'r') as f:
        for line in f:
            data.append(line)

    header = csv.reader(data, delimiter=",").next()
    reader = csv.reader(data[1:], delimiter=",")

    if reverse is True:
        sortedlist = sorted(reader, key=operator.itemgetter(colindex),reverse = True)
    else:
        sortedlist = sorted(reader, key=operator.itemgetter(colindex))
    os.remove(csvfile)
    ResultFile = open(csvfile,'wb')
    wr = csv.writer(ResultFile)
    wr.writerow(header)
    for l in sortedlist:
        wr.writerow(l)
    ResultFile.close()
    print "Finished sorting the csv"

def GetSHPcols(shapefile):
    """ This code returns a list version of Arcpy.ListFields(shapefile). I added this code to easily list fields without using Arcpy explicitly."""
    mylist = []
    for field in arcpy.ListFields(shapefile):
        mylist.append(str(field.name.strip()))

    return mylist

def RemoveSHPcols(shapefile, cols):
    """ This function removes any specified field from the shapefile if it exists. Column names must be no longer than 11 characters """
    for col in cols:
        col = col[:10]
        if arcpy.ListFields(shapefile, col):
            arcpy.DeleteField_management(shapefile, col)
            print 'Field deleted:', col
        else:
            print 'No field to delete:', col



def AddSHPcols(shapefile, cols, datatype):
    """ This function will add a new column of a specified datatype to the shapefile. Column names must be no longer than 11 characters The data types are specified here and should be passed a string. For many more detailed options, use arcpy.AddField_management().
        The field type of the new field.

        TEXT Any string of characters.
        FLOAT  Fractional numbers between -3.4E38 and 1.2E38.
        DOUBLE  Fractional numbers between -2.2E308 and 1.8E308.
        SHORT  Whole numbers between -32,768 and 32,767.
        LONG  Whole numbers between -2,147,483,648 and 2,147,483,647.
        DATE Date and/or time.
        BLOB Long sequence of binary numbers. You need a custom loader or viewer or a third-party application to load items into a BLOB field or view the contents of a BLOB field.
        RASTER Raster images. All ArcGIS software-supported raster dataset formats can be stored, but it is highly recommended that only small images be used.
        GUID Globally unique identifier.
    If you try to add a duplicate column that is already in the shapefile, the existing duplicate column will be deleted."""
    if type(cols) is list:
        for col in cols:
            col = col[:10]
            if arcpy.ListFields(shapefile, col):
                print 'Removed existing column from the shapefile:', col
                arcpy.DeleteField_management(shapefile, col)
                arcpy.AddField_management(shapefile, col, datatype)
            else:
                arcpy.AddField_management(shapefile, col, datatype)
            print 'Added column to the shapefile:', col, datatype
    else:
        col = cols[:10]
        if arcpy.ListFields(shapefile, col):
            print 'Removed existing column from the shapefile:', col
            arcpy.DeleteField_management(shapefile, col)
            arcpy.AddField_management(shapefile, col, datatype)
        else:
            arcpy.AddField_management(shapefile, col, datatype)
        print 'Added column to the shapefile:', col, datatype




def Join_CSV_to_SHP(csvfile, shapefile, shapefilejoincol, csvjoinindex, csvfieldindex):
    """ This function manually joins the CSV to the shapefile and does not use geodatabase tables like the JoinCSV() and JoinSHP() functions. This method should be easier and faster in most cases. In the CSV, the join column must be before the columns with mapping values. This code will map all fields from the mapping column onward (to the right). Returns missing cols. Column limit should be 10 characters."""

    cols = GetCSVcols(csvfile)

    i = 0
    newcols = []
    for col in cols:
        if i >= csvfieldindex:
            newcols.append(col[:10])
        i +=1

    AddSHPcols(shapefile, newcols, "double")
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

    rows = arcpy.UpdateCursor(shapefile)
    #rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (shapefilejoincol, method)) ##sorted
    shpjoinlist = []
    missingshpvals = []
    for row in rows:
        shpjoinval = str(row.getValue(shapefilejoincol))
        shpjoinlist.append(shpjoinval)
        try:
            vals = lib.get(shpjoinval)
            for ind, field in enumerate(newcols):
                row.setValue(str(field),float(vals[ind]))
                rows.updateRow(row)
        except:
            pass
            # missingshpvals.append(shpjoinval) #This is the shapefile value that there is no corresponding CSV value for. This list is for debugging.
    # missingcsvvals = []
    # for l in csvjoinlist:
    #     if l not in shpjoinlist:
    #         missingcsvvals.append(l)

    return #missingcsvvals #these values are missing

def JoinCSV(csvfile, workspace):
    """ This function will import the csv to the workspace. This datatable will then be imported to a shapefile using the JoinSHP() function. This returns a string of the workspace and table name"""
    tablename = os.path.basename(csvfile).rstrip('.csv')
    try:
        arcpy.Delete_management(workspace + '\\' + tablename)
        arcpy.TableToTable_conversion(csvfile, workspace, tablename)
        print "Old table in workspace deleted, replaced by new table ", workspace + '\\'+tablename
    except:
        arcpy.TableToTable_conversion(csvfile, workspace, tablename)
        print "New table in workspace added to the workspace with name ", workspace + '\\'+tablename
    return workspace + '\\'+tablename

def JoinSHP(jointable, joinfield, shapefile, shpjoinfield, add_fields):
    """ Joins the workspace table to the shapefile. The workspace table is generated by JoinCSV().  jointable and shapefile should be the full path of the file ie. C:\path\to\shapefile.shp and c:path\to\workspace.gbp\tablename """
    new_fields = []
    for col in add_fields:
        col = col[:10]
        new_fields.append(col)
        if arcpy.ListFields(shapefile, col):
            arcpy.DeleteField_management(shapefile, col)
    arcpy.JoinField_management(shapefile, shpjoinfield,jointable, joinfield, new_fields)
    print "Finished shapefile join."

def CheckMissingSHPVals(csvfile,joincol, shpfile, shpfileheader):
    """This script will check to see if any join column values in the CSV are missing in the shapefile. Returns a list of missing shapefile join data.CheckMissingSHPVals(csvfile should be a filepath. joincol is the column index in the csv starting at 0. shapefile is shapefile path. shapefile header should be the column lookup name.)"""
    csvvals = []
    with open(csvfile) as csv:
        csv.next()
        for l in csv:
            csvvals.append(l.split(',')[joincol])
    shpvals = []
    rows = arcpy.SearchCursor(shpfile,fields = shpfileheader)
    for row in rows:
        shpvals.append(str(row.getValue(shpfileheader)))
    results = []
    for val in csvvals:
        if val not in shpvals:
            results.append(val)
    if results == []:
        print "All values were joined"
    return results

def GetMXDList():
    return glob(os.path.join("C:\Mapping_Project\MXDs","*.mxd"))

def GetLayers(mxds):
    """Prints the available layers in the mxd document. A string version of the layer name is returned. GetLayers(mxds = 'mxdpath' or ['mxdpath1','mxdpath2'])"""

    lyrlist = []
    if type(mxds) is list:
        for mxdpath in mxds:
            print mxdpath
            mxd = arcpy.mapping.MapDocument(mxdpath)
            i = 0
            for lyr in arcpy.mapping.ListLayers(mxd):
                lyrlist.append([os.path.basename(mxdpath), str(lyr.name), i])
                i += 1
        print 'MXD\tLAYER\tLAYER_INDEX'
        for row in lyrlist:
            print row
        return lyrlist
    elif type(mxds) is str:
        mxd = arcpy.mapping.MapDocument(mxds)
        i = 0
        for lyr in arcpy.mapping.ListLayers(mxd):
            lyrlist.append([os.path.basename(mxds), str(lyr.name), i])
            i += 1
        print 'MXD\tLAYER\tLAYER_INDEX'
        for row in lyrlist:
            print row
        return lyrlist
    else:
        print "The mxd needs to be formatted as a list, not a string. add brackets around the variable ['mxdpath']"

def CreateMaps(mxds,shplyr,mapfields,symbology):
    """This function will create maps for all mxds specified and all fields in the mapfields list. The symbology options = 'Percent_Change' and 'Diff_LC'. If the symbology does not exist locally, this function will copy the necessary files from the network into the mxd\symbology folder. """

    if type(mxds) is str:
        newmxd = []
        newmxd.append(mxds)
        mxds = newmxd
    if type(mapfields) is str:
        newmapfields = []
        newmapfields.append(mapfields)
        mapfields = newmapfields

    mapresolution = 300 #300 is common.

    if symbology.lower() == "percent_change":
        symbpath = arcpy.mapping.Layer("C:\Mapping_Project\MXDs\Symbology\PercentChange.lyr")
    elif symbology.lower() == "diff_lc":
        symbpath = arcpy.mapping.Layer('C:\Mapping_Project\MXDs\Symbology\DifferenceinLossCost.lyr')
    else:
        print "You need to choose a symbology type: 'Percent_Change' or 'Diff_LC'"
        return
    for mxd in mxds:
        mxdobj = arcpy.mapping.MapDocument(mxd)
        df = arcpy.mapping.ListDataFrames(mxdobj)[0] #leave as default for these maps(will it change for other perils????)
        for lyr in arcpy.mapping.ListLayers(mxdobj):
            if lyr.name == shplyr: #leave as default for these maps(will it change for other perils????)
                lyr.symbologyType == "GRADUATED_COLORS"
                for field in mapfields:
                    arcpy.mapping.UpdateLayer(df, lyr, symbpath, True) #if you get a value error, it could be because of the layers source symbology no longer being available. It could also be because of a join issue or duplicate columns
                    lyr.symbology.valueField = field
                    arcpy.RefreshActiveView()
                    arcpy.mapping.ExportToJPEG(mxdobj, "C:\Mapping_Project\Out/"+ os.path.basename(mxd).rstrip('.mxd') +'_' + field + symbology +".jpg", resolution=mapresolution)


def CreateMaps2(mxds,shp1, shp2,  mapfields,symbology, labels1 = False,labels2 = False):
    """This function will create maps for all mxds specified and all fields in the mapfields list. The symbology options = 'Percent_Change' and 'Diff_LC'. If the symbology does not exist locally, this function will copy the necessary files from the network into the mxd\symbology folder. This function will show shplyr1's labels. The option expression field will update the labels. """

    if type(mxds) is str:
        newmxd = []
        newmxd.append(mxds)
        mxds = newmxd
    if type(mapfields) is str:
        newmapfields = []
        newmapfields.append(mapfields)
        mapfields = newmapfields

    mapresolution = 300 #300 is common.

    if symbology.lower() == "percent_change":
        symbpath = arcpy.mapping.Layer("C:\Mapping_Project\MXDs\Symbology\PercentChange.lyr")
    elif symbology.lower() == "diff_lc":
        symbpath = arcpy.mapping.Layer('C:\Mapping_Project\MXDs\Symbology\DifferenceinLossCost.lyr')
    else:
        print "You need to choose a symbology type: 'Percent_Change' or 'Diff_LC'"
        return
    for mxd in mxds:
        mxdobj = arcpy.mapping.MapDocument(mxd)
        df = arcpy.mapping.ListDataFrames(mxdobj)[0] #leave as default for these maps(will it change for other perils????)

        for lyr in arcpy.mapping.ListLayers(mxdobj):
            if lyr.name == os.path.basename(shp1).replace(".shp",""):
                lyr1 = lyr
            elif lyr.name == os.path.basename(shp2).replace(".shp",""):
                lyr2 = lyr

        lyr1.symbologyType == "GRADUATED_COLORS"
        lyr2.symbologyType == "GRADUATED_COLORS"

        for field in mapfields:
            field = field [:10]
            print os.path.basename(mxd).rstrip(".mxd"), field
            arcpy.mapping.UpdateLayer(df, lyr1, symbpath, True) #if you get a value error, it could be because of the layers source symbology no longer being available. It could also be because of a join issue or duplicate columns

            if symbology.lower() == "percent_change":
                expres = "str(int(round(float(["+field+"])*100,0))) + '%'"
            elif symbology.lower() == "diff_lc":
                expres = "str(int(round(float(["+field+"])*100,0)))"
            else:
                print "You need to pick a symbology."
                return
            lyr1.symbology.valueField = field
            if labels1 == True:
                if lyr1.supports("LABELCLASSES"):
                    lyr1.showLabels = True
                # print "Layer name: " + lyr1.name
                    for lblClass in lyr1.labelClasses:
                        lblClass.expression = expres
                        lblClass.SQLQuery = field +" <> -9999"
            else:
                lyr1.showLabels = False

            arcpy.mapping.UpdateLayer(df, lyr2, symbpath, True)
            lyr2.symbology.valueField = field

            if labels2 == True:
                if lyr2.supports("LABELCLASSES"):
                    lyr2.showLabels = True
                # print "Layer name: " + lyr2.name
                    for lblClass in lyr2.labelClasses:
                        lblClass.expression = expres
                        lblClass.SQLQuery = field +" <> -9999"
            else:
                lyr2.showLabels = False

            arcpy.RefreshActiveView()
            arcpy.mapping.ExportToJPEG(mxdobj, "C:\Mapping_Project\Out/"+ os.path.basename(mxd).rstrip('.mxd') +'_' + field + symbology +".jpg", resolution=mapresolution)



def CalculateField(shapefile, fieldname, py_expression):
    """Calculate values for a field given a python expression as a string. The py expression should be formatted with ! characters before and after the field name. ie.py_expression ='str(!POSTCODE!) + '_' + str(!JOIN!) """
    arcpy.CalculateField_management (shapefile, fieldname, py_expression,"Python")


def SortShapefile():
    """This script is not working. It can grab all of the values in the dbf, but not update them..."""
    pass

    #     fields = arcpy.ListFields(shpfile)
    # # for field in fields:
    # #     print field.name

    # newlst = []
    # rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (sort_field, method))
    # for row in rows:
    #     vals = []
    #     for field in fields:
    #         vals.append(row.getValue(field.name))
    #     newlst.append(vals)

    # rows = arcpy.UpdateCursor(shpfile,"","","","%s %s" % (sort_field, method))
    # vals = newlst[0]
    # for row in rows:
    #     print row
    #     print vals
    #     rows.updateRow(vals[0])
    #     vals = vals.next()
