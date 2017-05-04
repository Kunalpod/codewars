#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Build a pile of Cubes
#Problem level: 6 kyu

def find_nb(m):
    i = int((2*(m**0.5))**0.5)
    if ((i**2)*((i+1)**2))//4 == m:
        return i
    return -1   
