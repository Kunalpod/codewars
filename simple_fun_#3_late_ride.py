#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #3: Late Ride
#Problem level: 7 kyu

def late_ride(n):
    return sum([int(x) for x in list(str(n//60)+str(n%60))])
