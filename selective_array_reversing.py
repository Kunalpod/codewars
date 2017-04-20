#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Selective Array Reversing
#Problem level: 6 kyu

def sel_reverse(arr,l):
    li=[]
    if not l:
        return arr
    for i in range(0,len(arr),l):
        if i+l>len(arr):
            li+=(list(reversed(arr[i:])))
        else:   
            li+=(list(reversed(arr[i:i+l])))
    return li        
