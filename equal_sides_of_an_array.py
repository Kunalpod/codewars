#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Equal Sides Of An Array
#Problem level: 6 kyu

def find_even_index(arr):
    if not sum(arr[1:]): return 0
    if not sum(arr[:len(arr)-1]): return len(arr)-1
    for i in range(1, len(arr)-1):
        if sum(arr[:i])==sum(arr[i+1:]):
            return i    
    return -1        
