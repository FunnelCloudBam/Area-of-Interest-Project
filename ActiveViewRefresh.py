import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

#Process: refresh the view
arcpy.RefreshActiveView()