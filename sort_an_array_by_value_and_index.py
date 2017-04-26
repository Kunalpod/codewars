#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sort an array by value and index
#Problem level: 7 kyu

def key(ele):
    return ele[0] * ele[1]

def sort_by_value_and_index(arr):
    return [x[0] for x in sorted([[arr[x], x+1] for x in range(len(arr))], key=key)]
