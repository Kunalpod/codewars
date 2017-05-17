#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Perimeter of squares in a rectangle
#Problem level: 5 kyu

def fib(n):
    f = [0, 1, 1]
    for i in range(3,n):
        f.append(f[i-1]+f[i-2])
    return f[1:n]
    
def perimeter(n):
    return 4 * sum(fib(n+2))
