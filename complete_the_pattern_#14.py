#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #14
#Problem level: 6 kyu

def pattern(*args):
    n = args[0]
    y = 1 if len(args)==1 else args[1]
    s= ""
    if n<1:    return s
    if y<=1:    y = 1
    for i in range(y):
        x = 1 if i==0 else 2
        for j in range(x, n):
            s += ' '*(j-1) + str(j%10) + ' '*(2*(n-j)-1) + str(j%10) + ' '*(j-1) + '\n'
        s += ' '*(n-1) + str(n%10) + ' '*(n-1) + '\n'
        for j in reversed(list(range(1, n))):
            s += ' '*(j-1) + str(j%10) + ' '*(2*(n-j)-1) + str(j%10) + ' '*(j-1) + '\n'
    return s[:-1]
