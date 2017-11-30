import urllib.request
import numpy
import array
import sys

elevation_data = []



def fetch_elevation_data(min_long=-113.36, min_lat=36.0, max_long=-113.13, max_lat=36.23, resolution=30):

    if (resolution < 30):
        resolution = 30

    m_per_deg_lat = 111619
    deg_per_m = resolution / m_per_deg_lat

    long_range = max_long - min_long
    lat_range = max_lat - min_lat

    width = round(long_range / deg_per_m)
    height = round(lat_range / deg_per_m)

    res = urllib.request.urlopen('https://data.worldwind.arc.nasa.gov/elev?'
                                 'service=WMS'
                                 '&request=GetMap'
                                 '&layers=NED'
                                 '&crs=EPSG:4326'
                                 '&format=image/bil'
                                 '&transparent=FALSE'
                                 '&width=' + str(width) +
                                 '&height=' + str(height) +
                                 '&bgcolor=0xFFFFFF'
                                 '&bbox=' + str(min_long) + ',' + str(min_lat) + ',' + str(max_long) + ',' + str(max_lat) +
                                 '&styles='
                                 '&version=1.3.0')

    f = open('data.bil', 'wb')
    bytes_written = f.write(res.read())
    f.close()

    # Read from file again
    b = array.array("h")
    with open("data.bil", "rb") as f:
        b.fromfile(f, width * height)
    if sys.byteorder == "big":
        b.byteswap()

    for y in range(0, height):
        row = []
        for x in range(0, width):
            start = height * y
            row.append(b[start + x])
        elevation_data.append(row)

fetch_elevation_data()
print(elevation_data)