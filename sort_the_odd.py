#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sort the odd
#Problem level: 6 kyu

def sort_array(source_array):
    li=list(sorted([x for x in source_array if x%2], reverse=True))
    for i in range(len(source_array)):
        if source_array[i]%2:
            source_array[i]=li.pop()
    return source_array        
