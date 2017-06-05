#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Triangle number check
#Problem level: 6 kyu

def is_triangle_number(number):
    n = 0
    s = 1
    if not isinstance(number, int): return False
    while (n < number):
        n = n + s
        s = s + 1
    return n == number
