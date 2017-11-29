from owslib.wms import WebMapService




wms = WebMapService('http://webmap.ornl.gov/ogcbroker/wms', version='1.1.1')

gtopo = '10003_1'



print(wms[gtopo].title)
print(wms[gtopo].queryable)
print(wms[gtopo].opaque)
print(wms[gtopo].boundingBox)
print(wms[gtopo].boundingBoxWGS84)
print(wms[gtopo].crsOptions)
print(wms[gtopo].styles)

get_feature_info = wms.getOperationByName('GetFeatureInfo')
print(get_feature_info.formatOptions)

img = wms.getmap(layers=[gtopo],
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