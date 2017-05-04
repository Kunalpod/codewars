#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Are they the "same"?
#Problem level: 6 kyu

def comp(array1, array2):
    if array1==None or array2==None:    return False
    for a1 in array1:
        if a1**2 not in array2:
            return False
        array2.pop(array2.index(a1**2))
    if array2:    return False    
    return True
