#Not good enough
#fml

def find_all(sum_dig, dig):
    count=0
    
    if sum_dig>dig*9:
        return []
    if sum_dig==dig*9:
        return [1,int(str(9)*(dig)),int(str(9)*(dig))]
    
    mini = 10**(dig)
    maxi = 10**(dig-1)
    ma = 9
    mi = 1
    for i in range(1,10):
        if i*dig>=sum_dig:
            ma=i
            break  
    for i in range(0,dig+1):
        if i*9+1*(dig-i)<=sum_dig:
            mi=i
        else:
            break
    num = int('1'*(dig-mi) + '9'*mi)
    while(num<int(str(ma)*(dig))+1):
        if int(str(num)[0])*dig>sum_dig:
            break
        if int(''.join(sorted(str(num))))==num: 
            if sum([int(x) for x in str(num)])==sum_dig:
                count+=1
                if mini>num: mini=num
                if maxi<num: maxi=num
        if int(str(num)[-1])==9:
            num+=int(str(num)[-2])+2
        else:    num+=1    
    return [count, mini, maxi]
