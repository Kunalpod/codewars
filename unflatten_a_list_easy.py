#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Unflatten a List (Easy)
#Problem level: 7 kyu

def unflatten(arr):
    i = 0
    li = []
    while i<len(arr):
        if arr[i]<3:    
            li.append(arr[i])
            i+=1
        else:
            if i+arr[i]>=len(arr):
                li.append(arr[i:])
                break
            li.append(arr[i:i+arr[i]])
            i += arr[i]
    return li 
