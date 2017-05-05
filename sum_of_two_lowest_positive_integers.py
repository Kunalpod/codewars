#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sum of two lowest positive integers
#Problem level: 7 kyu

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
