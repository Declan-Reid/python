import PySimpleGUI as sg
import pyperclip


binary = ''

while True:
    layout = [  [sg.Text("Text to Binary:")],
                [sg.Input("Hello, World!"), sg.Button("Convert"), sg.Button("Copy Input"), sg.Button("Copy Output")],
                [sg.Text(binary)]   ]

    window = sg.Window('Binary Converter', layout)
    event, values = window.read()
    if event == 'Convert':
        binary = ''
        for i in values[0]:
            binary += "{0:08b}".format(ord(i))  # Creates binary version of chracter
            binary = binary+" "                 # Divides binary with space
        print(binary)
    if event == 'Copy Input':
        pyperclip.copy(values[0])
    if event == 'Copy Output':
        pyperclip.copy(binary)
    window.close()