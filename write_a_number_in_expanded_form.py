#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Write a number in expanded form
#Problem level: 6 kyu

def expanded_form(num):
    return ' + '.join([str(num)[x] + '0'* (len(str(num)) - 1 - x) for x in range(len(str(num))) if str(num)[x] != '0'])
