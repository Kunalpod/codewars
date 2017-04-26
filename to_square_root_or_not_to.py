#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: To square(root) or not to square(root)
#Problem level: 8 kyu

def square_or_square_root(arr):
    return [(int(x**0.5) if (x**0.5).is_integer() else int(x**2)) for x in arr]
