#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Calculator
#Problem level: 3 kyu

class Calculator(object):
  def evaluate(self, string):
    return float("%.4f"%eval(string))
