#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Number of People in the Bus
#Problem level: 8 kyu

def number(bus_stops):
    sum = 0
    for x in bus_stops:
        sum += x[0]-x[1]
    return sum    
