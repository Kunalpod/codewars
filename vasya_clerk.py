#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Vasya-Clark
#Problem level: 6 kyu

def tickets(people):
    collection=[0,0,0]
    for person in people:
        print(collection)
        if person==25:    collection[0]+=1
        elif person==50:
            if collection[0]>0:
                collection[0]-=1 
                collection[1]+=1
            else:    return "NO"
        elif person==100:
            if collection[0]>0 and collection[1]>0:
                collection[0]-=1
                collection[1]-=1
                collection[2]+=1
            elif collection[0]>=3:
                collection[0]-=3 
                collection[2]+=1
            else:
                return "NO"
    return "YES"
