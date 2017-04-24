#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #169: Press Button
#Problem level: 6 kyu

def press_button(n):
    return (n) + sum([x*(n-x) for x in range(1,n)])
