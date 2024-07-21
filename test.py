
import random




rows = int(input("enter the number of the rows for the game board : "))
columns = int(input("enter the numbers of the columns for the game board : "))

randRow = random.randint(0, rows)
randCol = random.randint(0, columns)

print(randRow, randCol)


tresureRow = int(input("choose a row to hide the treasure (1 - 5 ) : "))
tresureColumn = int(input("choose a column to hide the treasure (1 - 5 ) : "))



board = []




for _ in range(rows):
    row = ["*"] * columns
    board.append(row)



for i in range(rows):
    for j in range(columns):
     print(board[i][j], end = " ")
    
    print("\n")


print("diğer matris")


board[tresureRow - 1][tresureColumn - 1] = "T" 

for i in range(rows):
    for j in range(columns):
     print(board[i][j], end = " ")
    
    print("\n")





if randRow == tresureRow and randCol == tresureColumn:
   print("you found the treasure")
else:
   print("you didn't find the treasure")
