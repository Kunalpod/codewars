#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sum of the first nth term of Series
#Problem level: 7 kyu

def series_sum(n):
    if n == 0:    return "0.00"
    sum_series = round(sum([(1.0/(1+i*3)) for i in range(n)]), 2)
    return '{:0<4}'.format(sum_series)[:4]
