import PySimpleGUI as sg
from simpleeval import simple_eval

calcText = float()
perc = ''

# Create the window
while True:
    # Define the window's contents
    layout = [  [sg.Text(str(calcText)+perc)],
                [sg.Button("C"), sg.Button("+/-"), sg.Button("%"), sg.Button("÷")],
                [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("X")],
                [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("-")],
                [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("+")],
                [sg.Button("0"), sg.Button("00"), sg.Button("."), sg.Button("=")]    ]
    window = sg.Window('Window Title', layout)
    event, values = window.read()
    if event == '1':
        calcText = calcText * 10 + 1
    if event == '2':
        calcText = calcText * 10 + 2
    if event == '3':
        calcText = calcText * 10 + 3
    if event == '4':
        calcText = calcText * 10 + 4
    if event == '5':
        calcText = calcText * 10 + 5
    if event == '6':
        calcText = calcText * 10 + 6
    if event == '7':
        calcText = calcText * 10 + 7
    if event == '8':
        calcText = calcText * 10 + 8
    if event == '9':
        calcText = calcText * 10 + 9
    if event == '0':
        calcText = calcText * 10
    if event == '00':
        calcText = calcText * 100
    if event == 'C':
        if calcText != float():
            calcText = float(int(calcText / 10))
    if event == '+/-':
        calcText = calcText*(-1)
    if event == '%':
        if perc == '':
            perc = '%'
            calcText = calcText/100
        else:
            perc = ''
            calcText = calcText*100
    if event == sg.Button('='):
        calcText = simple_eval(calcText)
    
    print(calcText)
    window.close()
    

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or window.read call

# Do something with the information gathered

print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window