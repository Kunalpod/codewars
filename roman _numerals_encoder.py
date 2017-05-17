#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Roman Numerals Encoder
#Problem level: 4 kyu

def solution(n):
    str = ""
    if n//1000:
        str += 'M'*(n//1000)
        n = n % 1000
    if n//100:
        if n//100 == 9:
            str += "CM"
        elif n//100 >=5:
            str += "D" + "C"*(n//100 - 5)
        elif n//100 == 4:
            str += "CD"
        else:
            str += "C"*(n//100)
        n = n % 100    
    if n//10:
        if n//10 == 9:
            str += "XC"
        elif n//10 >= 5:
            str += "L" + "X"*(n//10 - 5)
        elif n//10 == 4:
            str += "XL"
        else:
            str += "X"*(n//10)
        n = n % 10
        
    if n == 9:
        str += "IX"
    elif n >= 5:
        str += "V" + "I"*(n - 5)
    elif n == 4:
        str += "IV"
    else:
        str += "I"*(n)
        
    return str            
