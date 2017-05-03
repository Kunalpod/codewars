#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Multiples of 3 and 5
#Problem level: 6 kyu

def solution(number):
    return sum([x for x in range(3,number) if x%3==0 or x%5==0])
