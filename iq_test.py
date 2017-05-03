#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: IQ Test
#Problem level: 6 kyu

def iq_test(numbers):
    odd = [int(x) for x in numbers.split() if int(x)%2]
    even = [int(x) for x in numbers.split() if not int(x)%2]
    return numbers.split().index(str(odd[0]))+1 if len(odd)==1 else numbers.split().index(str(even[0]))+1
