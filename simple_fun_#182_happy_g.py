#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #182: Happy "g"
#Problem level: 7 kyu

def happy_g(s):
  for i in range(len(s)):
      if s[i]=='g':
          if i==0 and s[i+1]!='g':
              return False
          if s[i-1]!='g' and s[i+1]!='g':
              return False
  return True      
