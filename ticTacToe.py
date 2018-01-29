theBoard={'1': ' ','2': ' ','3': ' ',
          '4': ' ','5': ' ','6': ' ',
          '7': ' ','8': ' ','9': ' '}


def printBoard(board):
    print(board['1'] + '|'+ board['2']+ '|'+ board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5']+ '|'+ board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8']+ '|'+board['9'])


def checkBoard(board):
    win=0
    if board['1']==board['2']==board['3']!=' ' or \
       board['1']==board['4']==board['7']!=' ' or \
       board['1']==board['5']==board['9']!=' ' or \
       board['2']==board['5']==board['8']!=' ' or \
       board['3']==board['6']==board['9']!=' ' or \
       board['3']==board['5']==board['7']!=' ' or \
       board['4']==board['5']==board['6']!=' ' or \
       board['7']==board['8']==board['9']!=' ':
        win=1
    return win



turn ='X'
printBoard(theBoard)

for i in range(9):
    print('turn for '+ turn +'. Move on which space?')
    move=input()
    if move==' ' or move =='':
        break
    theBoard[move]=turn
    printBoard(theBoard)
    winner=checkBoard(theBoard)
    if winner==1:
        print('Winner is '+ turn)
        break
    if turn=='X':
        turn='O'
    else:
        turn='X'

print('Game Over')
#printBoard(theBoard)
           
