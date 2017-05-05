#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Format a string of names like 'Bart, Lisa & Maggie'.
#Problem level: 6 kyu

def namelist(names):
    li= [x['name'] for x in names]
    if len(li) == 0:
        return ''
    elif len(li)>1: 
        return ', '.join(li[:-1]) + " & "+li[-1] 
    return li[0]
