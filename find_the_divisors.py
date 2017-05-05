#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the Divisors!
#Problem level: 6 kyu

def divisors(integer):
    li = [x for x in range(int(integer/2) + 1) if x!=0 and x!=1 and integer%x==0]
    if len(li)==0:
        return str(integer)+" is prime"
    else:
        return li
