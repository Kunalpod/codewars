#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Directions Reduction
#Problem level: 5 kyu

def dirReduc(arr):
    while(1):
        for i in range(len(arr)-1):
            if arr[i]=='':    continue
            if (arr[i][0]=='N' and arr[i+1][0]=='S') or (arr[i][0]=='S' and arr[i+1][0]=='N'):
                arr[i] = arr[i+1] = ''
            elif (arr[i][0]=='E' and arr[i+1][0]=='W') or (arr[i][0]=='W' and arr[i+1][0]=='E'):
                arr[i] = arr[i+1] = ''    
        if '' in arr:
            arr = [x for x in arr if x!='']
        else: return arr    
