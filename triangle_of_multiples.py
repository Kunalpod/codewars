#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Triangle of Multiples (Easy One)
#Problem level: 6 kyu

def mult_triangle(n):
    s_even = sum([x**3 for x in range(1,n+1) if not x%2]) + sum([2*x*sum([y for y in range(2,x) if not y%2]) for x in range(2,n+1) if x%2])
    s_odd = sum([x**3 for x in range(1,n+1)]) - s_even
    return [s_even+s_odd, s_even, s_odd]
