#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Growth of a Population
#Problem level: 7 kyu

def nb_year(p0, percent, aug, p):
    # your code
    if(p0>=p):
        return 0
    else:
        return 1+nb_year((p0+int(percent*p0/100)+aug), percent, aug, p)
