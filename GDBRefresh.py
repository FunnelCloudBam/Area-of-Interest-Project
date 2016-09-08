import arcpy

target_folder = "C:/working/AOI_GDB/AOI_GDB_Editor.sde"

#Process
arcpy.RefreshCatalog(target_folder)