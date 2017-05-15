#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: N-th Fibonacci
#Problem level: 6 kyu

def nth_fib(n):
    if n==1: return 0
    if n==2: return 1
    return nth_fib(n-1) + nth_fib(n-2)
