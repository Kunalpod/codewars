#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Twisted Sum
#Problem level: 6 kyu

def compute_sum(n):
    return sum([sum([int(y) for y in str(x)]) for x in range(1,n+1)])
