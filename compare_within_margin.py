#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Compare within Margin
#Problem level: 8 kyu

def close_compare(a, b, margin = 0):
    if a>b and a-b > margin:    return 1
    elif a<b and b-a > margin:    return -1
    else:    return 0
