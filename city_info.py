from shapely.geometry import mapping
from input_output import read_text
from input_output import write_shape
from apis import getlatlong
from apis import get_height_ahn2
from geobuilder import point
# files
in_cities = "cities.txt"
out_shapefile = "/home/user/geocities/city_info_result.shp"
# data look like this

schema = {"geometry": "Point",
          "properties": {"city": "str","height": "float"}}

# store results in a list
result = []
# read text with cities
cities = read_text(in_cities)
# main loop
for city in cities:
    city = city.strip()
    print city
    location = getlatlong(city)
    print location
    geometry = point(location["lng"],location["lat"])
    geometry_wkt = geometry.wkt
    height = get_height_ahn2(geometry_wkt)
    result.append({"geometry":mapping(geometry),
                    "properties":{"city": city,"height": height}})
    
# save the results to sh
write_shape(out_shapefile,schema,result)
