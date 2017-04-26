#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Geometry Basics: Distance between points in 2D
#Problem level: 8 kyu

from math import sqrt
def distance_between_points(a, b):
    return sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
