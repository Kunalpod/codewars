#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Boolean Logic from Scratch
#Problem level: 7 kyu

def func_or(a,b):
    #your code here - do no be lame and do not use built-in code!
    if bool(a) or bool(b):
        return True
    return False    

def func_xor(a,b):
    #your code here - remember to consider truthy and falsey value as in JS
    if bool(a)==bool(b):
        return False
    return True 
