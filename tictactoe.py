
 
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWin(turn):
    list_of_marks = list()
    count = 0
    for key,value in theBoard.items():
        if value == turn:
            list_of_marks.append(key)
    for space in list_of_marks:
        if 'top' in space:
            count += 1
            if count == 3:
                return True
    count = 0
    for space in list_of_marks:
        if 'mid' in space:
            count += 1
            if count == 3:
                return True
    count = 0
    for space in list_of_marks:
        if 'low' in space:
            count += 1
            if count == 3:
                return True

    if 'top-L' in list_of_marks and 'mid-M' in list_of_marks and 'low-R' in list_of_marks:
        return True
    if 'low-L' in list_of_marks and 'mid-M' in list_of_marks and 'top-R' in list_of_marks:
        return True

    


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if(theBoard[move] != 'X' and theBoard[move] != 'O'):
        theBoard[move] = turn
    if checkWin(turn):
        print(turn + ' won!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)