from math import radians, cos, sin, asin, sqrt
from time import sleep
import geocoder

g = geocoder.ip('me')

a=(g.lng)
b=(g.lat)
c=(g.lng)
d=(g.lat)

print(a)
print(b)

sleep(2)

print(c)
print(d)



def haversine(lon1, lat1, lon2, lat2):
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1


    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = distance = 2 * asin(sqrt(a))
    r = 6371
    z= c * r
    print(z)


def image_file():
    haversine(a,b,c,d)
