#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #8: Kill K-th Bit
#Problem level: 7 kyu

def kill_kth_bit(n, k):
    b = list(bin(n))[2:]
    if len(b)>=k:
        b[(-1)*k]='0'
    return int(''.join(b),2)
