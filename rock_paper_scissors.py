#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Rock Paper Scissors!
#Problem level: 8 kyu

def rps(p1, p2):
    if p1[0]=='r' and p2[0]=='s':    return "Player 1 won!"
    if p1[0]=='s' and p2[0]=='p':    return "Player 1 won!"
    if p1[0]=='p' and p2[0]=='r':    return "Player 1 won!"
    if p2[0]=='r' and p1[0]=='s':    return "Player 2 won!"
    if p2[0]=='s' and p1[0]=='p':    return "Player 2 won!"
    if p2[0]=='p' and p1[0]=='r':    return "Player 2 won!"
    if p1==p2:    return 'Draw!'
