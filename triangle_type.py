#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Triangle Type
#Problem level: 6 kyu

def triangle_type(a, b, c):
    if a>=b+c or b>=c+a or c>=a+b:    return 0                                          #Not a triangle
    elif a**2 > b**2 + c**2 or b**2 > c**2 + a**2 or c**2 > a**2 + b**2: return 3       #Obtuse Triangle
    elif a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2: return 2    #Right-angle triangle
    else:    return 1                                                                   #Acute Triangle
