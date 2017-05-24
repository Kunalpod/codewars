#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Fizz Buzz Cuckoo Clock
#Problem level: 7 kyu

def fizz_buzz_cuckoo_clock(time):
    if int(time[3:]) == 0: 
        if int(time[:2])==0: return ("Cuckoo "*12)[:-1]
        return ("Cuckoo "*int(time[:2]))[:-1] if int(time[:2])<=12 else ("Cuckoo "*(int(time[:2])-12))[:-1]
    elif int(time[3:]) == 30: return "Cuckoo"
    elif not int(time[3:])%3 and not int(time[3:])%5:    return "Fizz Buzz"
    elif not int(time[3:])%3: return "Fizz"
    elif not int(time[3:])%5: return "Buzz"
    else: return "tick"
