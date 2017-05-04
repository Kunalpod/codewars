#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Delete occurrences of an element if it occurs more than n times
#Problem level: 6 kyu

def delete_nth(order,max_e):
    i=0
    while(i<len(order)):
        if order[:i].count(order[i])>=max_e:
            order.pop(i)
        else:    i+=1    
    return order
