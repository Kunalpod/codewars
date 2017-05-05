#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Highest and Lowest
#Problem level: 7 kyu

def high_and_low(numbers):
    # ...
    li = [int(x) for x in numbers.split()]
    numbers = str(max(li)) + " " + str(min(li))
    return numbers
