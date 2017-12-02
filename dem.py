import sys
import os
import array
import urllib.request
import math
import numpy as np
from scipy.spatial import Delaunay
import utm

elevation_data = []
m_per_deg_lat = 111619

def fetch_elevation_data(min_long=-113.36, min_lat=36.0, max_long=-113.13, max_lat=36.23, resolution=30):

    if (resolution < 30):
        resolution = 30

    resolution_in_deg = resolution / m_per_deg_lat

    long_range = max_long - min_long
    lat_range = max_lat - min_lat

    width = round(long_range / resolution_in_deg)
    height = round(lat_range / resolution_in_deg)

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

    # Read from file
    b = array.array("h")
    with open("data.bil", "rb") as f:
        b.fromfile(f, width * height)
    if sys.byteorder == "big":
        b.byteswap()

    for x in range(0, width):
        row = []
        for y in range(0, height):
            start = height * x
            row.append(b[start + y])
        elevation_data.append(row)
# end function


def elevation_points_to_xyz(min_long=-113.36, min_lat=36.0, max_long=-113.13, max_lat=36.23, resolution=30):

    resolution_in_deg = resolution / m_per_deg_lat

    data = []

    for i in range(0, len(elevation_data)):
        for j in range(0, len(elevation_data[0])):
            long = min_long + resolution_in_deg * j
            lat = max_lat - resolution_in_deg * i
            (x, y, _, _) = utm.from_latlon(lat, long)
            z = elevation_data[i][j]
            element = [x, y, z]
            data.append(element)

    xs = list(map(lambda e: e[0], data))
    ys = list(map(lambda e: e[1], data))
    zs = list(map(lambda e: e[2], data))

    mean_x = math.floor(max(xs) / min(xs))
    mean_y = math.floor(max(ys) / min(ys))
    min_z = math.floor(min(zs))

    data.append([min(xs) - 10, min(ys) - 10, min_z - 1])
    data.append([min(xs) - 10, max(ys) + 10, min_z - 1])
    data.append([max(xs) + 10, min(ys) - 10, min_z - 1])
    data.append([max(xs) + 10, max(ys) + 10, min_z - 1])

    return list(map(lambda e: [e[0] - mean_x, e[1] - mean_y, e[2] - min_z], data))
# end function


def write_points_to_obj():

    os.remove("model.obj")
    f = open("model.obj", 'a')

    minlong=-79.75
    minlat=37.5
    maxlong=-79.25
    maxlat=38
    resolution=90

    fetch_elevation_data(min_long=minlong, min_lat=minlat, max_long=maxlong, max_lat=maxlat, resolution=resolution)
    long_lat_data = elevation_points_to_xyz(min_long=minlong, min_lat=minlat, max_long=maxlong, max_lat=maxlat, resolution=resolution)

    for point in long_lat_data:
        f.write("v " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]) + '\n')

    long_lat_minus_elevation = np.array(list(map(lambda x: [x[0], x[1]], long_lat_data)))

    delauny = Delaunay(long_lat_minus_elevation)

    a = len(long_lat_data) - 1
    b = len(long_lat_data) - 2
    c = len(long_lat_data) - 3
    d = len(long_lat_data) - 4

    for simplex in delauny.simplices:
        # don't compute for (0,0) or (width,height)
        if (simplex[0] != a and
            simplex[1] != a and
            simplex[2] != a and
            simplex[0] != b and
            simplex[1] != b and
            simplex[2] != b and
            simplex[0] != c and
            simplex[1] != c and
            simplex[2] != c and
            simplex[0] != d and
            simplex[1] != d and
            simplex[2] != d):
            f.write("f " + str(simplex[0] + 1) + " " + str(simplex[1] + 1) + " " + str(simplex[2] + 1) + '\n')

    f.close()
# end function

write_points_to_obj()