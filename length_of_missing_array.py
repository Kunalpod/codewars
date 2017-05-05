#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Length of missing array
#Problem level: 6 kyu

def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays : return 0
    if None in array_of_arrays or [] in array_of_arrays: return 0
    li = list(sorted([len(x) for x in array_of_arrays]))
    for i in range(1,len(li)):
        if li[i]!=li[i-1]+1:
            return li[i-1]+1     
