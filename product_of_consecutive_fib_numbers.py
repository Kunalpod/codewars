#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Product of consecutive Fib numbers
#Problem level: 5 kyu

def gen_fib(num):
    fib = [0,1]
    while(fib[-1] <= num):
        fib.append(fib[-2]+fib[-1])
    return fib

def productFib(prod):
    fib = gen_fib(int(prod/2))
    for i in range(len(fib)-1):
        if fib[i]*fib[i+1] == prod:
            return [fib[i], fib[i+1], True]
        if fib[i]*fib[i+1] > prod:
            return [fib[i], fib[i+1], False] 
