#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Fibonacci Reloaded
#Problem level: 6 kyu

def fib(n, feeb=[0,1]):
    if n==0: return 1
    if n<=len(feeb): return feeb[n-1]
    else:
        for i in range(len(feeb),n+1): feeb.append(feeb[i-1]+feeb[i-2])
        return feeb[n-1]
