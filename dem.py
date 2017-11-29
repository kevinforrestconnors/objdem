from owslib.wms import WebMapService




wms = WebMapService('http://webmap.ornl.gov/ogcbroker/wms', version='1.1.1')

layer = list(wms.contents)[1]

print(wms[layer].title)
print(wms[layer].queryable)
print(wms[layer].opaque)
print(wms[layer].boundingBox)
print(wms[layer].boundingBoxWGS84)
print(wms[layer].crsOptions)
print(wms[layer].styles)

get_map = wms.getOperationByName('GetMap')
print(get_map.formatOptions)

img = wms.getmap(layers=[layer],
                 styles=['default'],
                 srs='EPSG:4326',
                 bbox=(-180, -90, 180, 90),
                 size=(600, 300),
                 format='image/tiff',
                 transparent=True
                 )
out = open('jpl_mosaic_visb.jpg', 'wb')
out.write(img.read())
out.close()