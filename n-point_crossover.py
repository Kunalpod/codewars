#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: N-Point Crossover
#Problem level: 6 kyu

def crossover(ns, xs, ys):
    for i in range(len(ns)):
        if ns[:i].count(ns[i]) > 0: continue
        t = xs[ns[i]:]
        xs = xs[:ns[i]] + ys[ns[i]:]
        ys = ys[:ns[i]] + t
    print(xs,ys)    
    return (xs,ys)
