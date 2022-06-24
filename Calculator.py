import PySimpleGUI as sg                        # Part 1 - The import

calcText = ""

# Define the window's contents
layout = [  [sg.Input(calcText)],     # Part 2 - The Layout
            [sg.Button("AC"), sg.Button("+/-"), sg.Button("%"), sg.Button("÷")],
            [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("X")],
            [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("-")],
            [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("+")],
            [sg.Button("0"), sg.Button("00"), sg.Button("."), sg.Button("=")]    ]

# Create the window
while True:
    window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or window.read call

# Do something with the information gathered

print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window