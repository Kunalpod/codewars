#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: First non-repeating letter
#Problem level: 5 kyu

def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ""        
