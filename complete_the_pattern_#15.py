#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #15
#Problem level: 6 kyu

def pattern(*args):
    n = args[0]
    x = 1 if len(args)<=1 else args[1]
    y = 1 if len(args)<=2 else args[2]
    s= ""
    if n<1:    return s
    if x<=1:    x = 1
    if y<=1:    y = 1

    for i in range(y):
        b = 1 if i==0 else 2
        for j in range(b, n):
            if j==1:    s += str(j%10) + ''.join([' '*(2*(n-j)-1) + str(j%10) for c in range(x)]) + '\n'
            else:    s += ' '*(j-1) + (' '*(2*j-3)).join([str(j%10) + ' '*(2*(n-j)-1) + str(j%10) for c in range(x)]) + ' '*(j-1) + '\n'
        s += ' '*(n-1) + (' '*(2*n-3)).join([str(n%10) for c in range(x)]) + ' '*(n-1) + '\n'
        for j in reversed(list(range(1, n))):
            if j==1:    s += str(j%10) + ''.join([' '*(2*(n-j)-1) + str(j%10) for c in range(x)]) + '\n'
            else:    s += ' '*(j-1) + (' '*(2*j-3)).join([str(j%10) + ' '*(2*(n-j)-1) + str(j%10) for c in range(x)]) + ' '*(j-1) + '\n'
    
    return s[:-1]
