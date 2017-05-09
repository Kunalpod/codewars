#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Moving Zeroes To The End
#Problem level: 5 kyu

def move_zeros(array):
    return [x for x in array if (str(x)!='0' and str(x)!='0.0') or x=='0'] + [x for x in array if (str(x)=='0' or str(x)=='0.0') and x!='0']
