#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sudoku Solution Validator
#Problem level: 4 kyu

def validSolution(board):
    for row in board:
        for i in range(1,10):
            if row.count(i)>1:    return False
    
    li = [[row[i] for row in board] for i in range(0,9)]
    for row in li:
        for i in range(1,10):
            if row.count(i)>1:    return False
            
    for i in range(0,9,3):
        for j in range(0,9,3):
            li = [board[i][j],board[i][j+1],board[i][j+2],board[i+1][j],board[i+1][j+1],board[i+1][j+2],board[i+2][j],board[i+2][j+1],board[i+2][j+2]]
            for x in range(1, 10):
                if li.count(x)>1:    return False
    
    return True
