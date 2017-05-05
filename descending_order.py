#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Descending Order
#Problem level: 7 kyu

def Descending_Order(num):
    return int(''.join([x for x in sorted(str(num), reverse=True)]))
