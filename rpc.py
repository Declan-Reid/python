import PySimpleGUI as sg
import random

while True:
    val = random.randint(1, 3)
    layout = [  [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors')] ]

    window = sg.Window('Rock Paper Scissors', layout)
    event, values = window.read()
    window.close()
    if event == 'Rock':
        if val == 1:
            layout = [  [sg.Text('Tie!'), sg.Button('Ok')]   ]
        if val == 2:
            layout = [  [sg.Text('You Lose!'), sg.Button('Ok')]   ]
        if val == 3:
            layout = [  [sg.Text('You Win!'), sg.Button('Ok')]   ]
    elif event == 'Paper':
        if val == 1:
            layout = [  [sg.Text('You Win!'), sg.Button('Ok')]   ]
        if val == 2:
            layout = [  [sg.Text('Tie!'), sg.Button('Ok')]   ]
        if val == 3:
            layout = [  [sg.Text('You Lose!'), sg.Button('Ok')]   ]
    elif event == 'Scissors':
        if val == 1:
            layout = [  [sg.Text('You Lose!'), sg.Button('Ok')]   ]
        if val == 2:
            layout = [  [sg.Text('You Win!'), sg.Button('Ok')]   ]
        if val == 3:
            layout = [  [sg.Text('You Tie!'), sg.Button('Ok')]   ]
    else:
        print('Process Killed.')
        exit()
    window = sg.Window('Rock Paper Scissors', layout)
    event, values = window.read()
    if event == sg.CloseButton:
        print('Process Killed.')
        exit()
    window.close()