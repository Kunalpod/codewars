#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Sentences
#Problem level: 6 kyu

def make_sentences(parts):
    li = parts[0]
    for x in parts[1:]:
        if x == ',':    li += x
        elif x[0]=='.': li += '.' if li[-1]!='.' else ''
        else: li += ' '+x
    return li if li[-1]=='.' else li+'.'    
