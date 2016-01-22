import requests


def getlatlong(query):
    """Get laittitude and longtitude from google api for a place

    Args:
        query (str): place to geocode

    Retruns:
        location in latlon
        
    """
    result = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address={}".format(query))
    location = result.json()["results"][0]["geometry"]["location"]
    return location

def get_height_ahn2(wkt_geom):
    """het AHN height from WKT geometry
    ARGS wkt_geom geometry as WKT

    Returns:
        height in mnap
    
    """
    result = requests.get("https://nxt.staging.lizard.net/api/v2/raster-aggregates/?agg=curve&geom={}&raster_names=dem%2Fnl&srs=EPSG:4326&start=2016-01-22T12:06:45&stop=2016-01-22T18:06:45&window=300000".format(wkt_geom),verify=False)
    print result.json()["data"][0]
    height = result.json()["data"][0]
    return height

    
