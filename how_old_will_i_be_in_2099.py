#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: How old will I be in 2099?
#Problem level: 8 kyu

def calculate_age(yob, cy):
    if yob == cy:    return "You were born this very year!"
    y = abs(yob - cy)
    if y == 1:
        return "You will be born in " + str(y) + " year." if yob>cy else "You are " + str(y) + " year old."
    return "You will be born in " + str(y) + " years." if yob>cy else "You are " + str(y) + " years old."
