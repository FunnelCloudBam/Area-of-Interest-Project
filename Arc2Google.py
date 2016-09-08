#Script Author: Noel Dyer
#Original file name was Arc2Google2.0.py
#Changed file name to Arc2Google.py - Joel Harrington


import webbrowser, arcpy, sys

MXD = arcpy.mapping.MapDocument('CURRENT')
df = arcpy.mapping.ListDataFrames(MXD)[0]

GoogleScales = [591657550.5, 295828775.3, 147914387.6, 73957193.82, 36978596.91, 18489298.45, 9244649.227,\
                4622324.614, 2311162.307, 1155581.153, 577790.5767, 288895.2884, 144447.6442, 72223.82209,\
                36111.91104, 18055.95552, 9027.977761, 4513.98888, 2256.99444, 1128.49722]
currentScale = df.scale
current = 0
previous = 591657550
z = 0
counter = 0 

for scale in GoogleScales:
    current = math.fabs(currentScale - scale)
    if current < previous:
        previous = current
        z = counter
    counter += 1

X = (df.extent.XMin + df.extent.XMax)/2
Y = (df.extent.YMin + df.extent.YMax)/2
CentroidOrigProj = arcpy.Point(X,Y)

WebM = arcpy.SpatialReference(4326)
PG = arcpy.PointGeometry(CentroidOrigProj, df.spatialReference)
CentroidProj = PG.projectAs(WebM)

WKTlist = CentroidProj.WKT.replace('(', ' ').replace(')', ' ').split()
projX = str(WKTlist[1])
projY = str(WKTlist[2])

GoogleEarth = 'http://maps.google.com/?ll=' + str(projY) + ',' + str(projX) + '&t=k' + '&z=' + str(z)
webbrowser.open_new_tab(GoogleEarth)
