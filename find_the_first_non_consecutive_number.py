#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the first non-consecutive number
#Problem level: 8 kyu

def first_non_consecutive(arr):
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    return None 
