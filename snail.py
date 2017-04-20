#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Snail
#Problem level: 4 kyu

def snail(array):
    li = []
    if not len(array[0]):
        return li
    while array:
        l = len(array)
        for i in range(0, l):
            li.append(array[0][i])
        array=array[1:]
        for i in range(0, l-1):
            li.append(array[i][-1])
            array[i] = array[i][:-1]
        for i in reversed(range(0, l-1)):
            li.append(array[-1][i])
        array=array[:-1]
        for i in reversed(range(0, l-2)):
            li.append(array[i][0])
            array[i] = array[i][1:]
    return li
