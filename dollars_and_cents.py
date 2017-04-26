#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Dollars and Cents
#Problem level: 8 kyu

def format_money(amount):
    d = str(amount).split('.')[0]
    c = '00' if amount==int(amount) else str(amount).split('.')[1]
    return '$'+d+'.'+(c if len(c)==2 else c+'0')
