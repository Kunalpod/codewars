#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Most digits
#Problem level: 7 kyu

def find_longest(arr):
    return arr[[len(str(x)) for x in arr].index(max([len(str(x)) for x in arr]))]
