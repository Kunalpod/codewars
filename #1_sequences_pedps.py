#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: #1 Sequences: Pure Even Digit Perfect Squares (P.E.D.P.S)
#Problem level: 6 kyu

def even_digit_squares(a, b):
    a = int(a ** 0.5)
    b = int(b ** 0.5)
    return [x**2 for x in range(a+1,b+1) if not [x for x in str(x**2) if int(x)%2]]
