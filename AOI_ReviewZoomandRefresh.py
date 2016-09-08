import arcpy

target_folder = "C:/working/AOI_GDB/AOI_GDB_Editor.sde"

#Process refresh GDB1
arcpy.RefreshCatalog(target_folder)

#get layer and add it into TOC
LayerPath = arcpy.GetParameterAsText(0)
addLayer = arcpy.mapping.Layer(LayerPath)
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

#adds the layer
arcpy.mapping.AddLayer(df, addLayer, "TOP")

#mxd = arcpy.mapping.MapDocument("CURRENT")
#df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "AOI_Review", df)[0]

#  select layer and zoom to the selection
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION")
df.zoomToSelectedFeatures()

# Edit selected features
#workspace = r"C:/working/AOI_GDB/AOI_GDB_Editor.sde"
#edit = arcpy.da.Editor(workspace)
#edit.startEditing()
#edit.startOperation()