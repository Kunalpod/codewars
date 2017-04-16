#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Give me a Diamond
#Problem level: 6 kyu

def diamond(n):
    if n%2==0 or n<1:
        return null
    li = []
    li += [''.join([' ' for _ in range(int((n-x)/2))]) + ''.join('*' for _ in range(x))+'\n' for x in range(n) if x%2==1]
    li += [("{:^"+str(n)+"}").format(''.join(['*' for _ in range(n)]))+'\n']
    li +=  [''.join([' ' for _ in range(int((n-x)/2))]) + ''.join('*' for _ in range(x))+'\n' for x in list(reversed(range(n))) if x%2==1]
    return ''.join(li)
