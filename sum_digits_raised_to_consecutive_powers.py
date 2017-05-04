#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
#Problem level: 6 kyu

def get_sum(n):
    x = str(n)
    sum = 0
    for i in range(len(x)):
        sum+= int(x[i])**(i+1)
    return sum    

def sum_dig_pow(a, b):
    return [n for n in range(a,b+1) if n==get_sum(n)]
