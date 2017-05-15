#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Exercise in Summing
#Problem level: 6 kyu

def minimum_sum(values, n):
    if n==0: return 0
    return sum(sorted(values)[:n])

def maximum_sum(values, n):
    if n==0: return 0
    return sum(sorted(values, reverse=True)[:n])
