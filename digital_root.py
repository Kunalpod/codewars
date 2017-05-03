#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sum of Digits / Digital Root
#Problem level: 6 kyu

def digital_root(n):
    if n//10==0:
        return n
    return digital_root(sum([int(x) for x in str(n)]))
