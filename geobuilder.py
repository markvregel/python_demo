from shapely.geometry import Point


def point(lat,lon, srs="EPSG:4326"):
    """Create a shapely Point geometry from lat and lon strings

        Arg:
            lat (str): lattitude
            lon (str): longtitude

        Return:
            schapely point object
    """
    return Point(float(lat), float(lon))
help(Point)
