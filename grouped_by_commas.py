#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Grouped by commas
#Problem level: 6 kyu

def group_by_commas(n):
    n = list(str(n))[::-1]
    li = []
    for i in range(len(n)):
        if i%3 == 2 and i+1 != len(n): li = li + [n[i]] + [',']
        else:    li = li + [n[i]]
    return ''.join(li[::-1])
