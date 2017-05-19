#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Pick peaks
#Problem level: 4 kyu

def pick_peaks(arr):
    print(arr)
    dic = {'pos':[], 'peaks':[] }
    for i in range(1,len(arr)-1):
        if arr[i]>=arr[i+1] and arr[i-1]<arr[i]:
            p = True
            if arr[i+1]!=arr[i]:    p = False
            for x in arr[i+1:]:
                if x > arr[i]:    break
                elif x<arr[i]:
                    p=False
                    break   
            if not p:
                dic['pos'].append(i)
                dic['peaks'].append(arr[i])
    return dic    
