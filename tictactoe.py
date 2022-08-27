import random

board = {
    'LT': ' ', 'T': ' ', 'RT': ' ',
    'L': ' ', 'C': ' ', 'R': ' ',
    'LB': ' ', 'B': ' ', 'RB': ' '
}

def checkFull():
    if board['LT'] != ' ' and board['T'] != ' ' and board['RT'] != ' ' and board['L'] != ' ' and board['C'] != ' ' and board['R'] != ' ' and board['LB'] != ' ' and board['B'] != ' ' and board['RB'] != ' ':
        return True
    else:
        return False

def user():
    inp = ''
    while inp != 'LT' and inp != 'T' and inp != 'RT' and inp != 'L' and inp != 'C' and inp != 'R' and inp != 'LB' and inp != 'B' and inp != 'RB':
        inp = input('Choose from the following: LT and T and RT and L and C and R and LB and B and RB\nMy Choice: ')
    if board[inp] == ' ':
        board[inp] = 'X'
        print(' '+board['LT']+' │ '+board['T']+' │ '+board['RT']+' ')
        print('⎯⎯⎯┼⎯⎯⎯┼⎯⎯⎯')
        print(' '+board['L']+' │ '+board['C']+' │ '+board['R']+' ')
        print('⎯⎯⎯┼⎯⎯⎯┼⎯⎯⎯')
        print(' '+board['LB']+' │ '+board['B']+' │ '+board['RB']+' ')
        return True
    else:
        print('That spot is taken')
        return False

def userTwo():
    inp = ''
    while inp != 'LT' and inp != 'T' and inp != 'RT' and inp != 'L' and inp != 'C' and inp != 'R' and inp != 'LB' and inp != 'B' and inp != 'RB':
        inp = input('Choose from the following: LT and T and RT and L and C and R and LB and B and RB\nMy Choice: ')
    if board[inp] == ' ':
        board[inp] = 'O'
        print(' '+board['LT']+' │ '+board['T']+' │ '+board['RT']+' ')
        print('⎯⎯⎯┼⎯⎯⎯┼⎯⎯⎯')
        print(' '+board['L']+' │ '+board['C']+' │ '+board['R']+' ')
        print('⎯⎯⎯┼⎯⎯⎯┼⎯⎯⎯')
        print(' '+board['LB']+' │ '+board['B']+' │ '+board['RB']+' ')
        return True
    else:
        print('That spot is taken')
        return False

def checkWin():
    if board['LT'] == 'X' and board['T'] == 'X' and board['RT'] == 'X':
        return 'X'
    elif board['LT'] == 'O' and board['T'] == 'O' and board['RT'] == 'O':
        return 'O'
    elif board['L'] == 'X' and board['C'] == 'X' and board['R'] == 'X':
        return 'X'
    elif board['L'] == 'O' and board['C'] == 'O' and board['R'] == 'O':
        return 'O'
    elif board['LB'] == 'X' and board['B'] == 'X' and board['RB'] == 'X':
        return 'X'
    elif board['LB'] == 'O' and board['B'] == 'O' and board['RB'] == 'O':
        return 'O'
    elif board['LT'] == 'X' and board['L'] == 'X' and board['LB'] == 'X':
        return 'X'
    elif board['LT'] == 'O' and board['L'] == 'O' and board['LB'] == 'O':
        return 'O'
    elif board['RT'] == 'X' and board['R'] == 'X' and board['RB'] == 'X':
        return 'X'
    elif board['RT'] == 'O' and board['R'] == 'O' and board['RB'] == 'O':
        return 'O'
    elif board['T'] == 'X' and board['C'] == 'X' and board['B'] == 'X':
        return 'X'
    elif board['T'] == 'O' and board['C'] == 'O' and board['B'] == 'O':
        return 'O'
    elif board['LT'] == 'X' and board['C'] == 'X' and board['RT'] == 'X':
        return 'X'
    elif board['LT'] == 'O' and board['C'] == 'O' and board['RT'] == 'O':
        return 'O'
    elif board['LB'] == 'X' and board['C'] == 'X' and board['RB'] == 'X':
        return 'X'
    elif board['LB'] == 'O' and board['C'] == 'O' and board['RB'] == 'O':
        return 'O'
    else:
        return False

while True:
    user()
    if checkWin() == 'X':
        print('X wins!')
        break
    elif checkWin() == 'O':
        print('O wins!')
        break
    if checkFull():
        print('Tie!')
        break
    userTwo()
    if checkFull():
        print('Tie!')
        break
    if checkWin() == 'X':
        print('X wins!')
        break
    elif checkWin() == 'O':
        print('O wins!')
        break