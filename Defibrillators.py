'''
 * User: Hojun Lim
 * Date: 2020-04-17
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
n = int(input())
distance = sys.maxsize # maximum value of possible integer
closest_fib = []

for i in range(n):
    defib = input()
    def_id, def_name, def_address, def_phone, def_lon, def_lat = defib.split(';')
    def_lon = float(def_lon.replace(',','.'))
    def_lat = float(def_lat.replace(',','.'))

    x = (math.radians(def_lon) - math.radians(lon))*math.cos(math.radians((def_lat+lat)/2))
    y = math.radians(def_lat) - math.radians(lat)
    d = math.sqrt(x**2+y**2)*6371 # calculate the distance between point (lon, lan) and (def_lon, def_lan)

    if d < distance:
        distance = d
        closest_fib = [def_name]

    elif d == distance:
        closest_fib.append(def_name)

for fib in closest_fib:
    print(fib)
