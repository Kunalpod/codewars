#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Tribonacci Sequence
#Problem level: 6 kyu

def tribonacci(arr,n):
    if n<=len(arr):    return arr[:n]
    for i in range(3,n):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    return arr
