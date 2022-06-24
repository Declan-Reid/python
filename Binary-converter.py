# This script will convert from binary to text and vice versa.

import os
os.system('clear')

def binary_to_text(binary):
    """
    This function will convert a binary string to a text string.
    """
    text = ""
    binary = binary.replace(" ", "")        #Removeallspacestoconverttext
    for i in range(0, len(binary), 8):      #Foreverygroupofeightcharacters:
        text += chr(int(binary[i:i+8], 2))  #Converttotextandaddittostring"text"
    return text

def text_to_binary(text):
    """
    This function will convert a text string to a binary string.
    """
    binary = ""
    for i in text:
        binary += "{0:08b}".format(ord(i))  # Creates binary version of chracter
        binary = binary+" "                 # Divides binary with space
    return binary

def main():
    """
    This function will run the program.
    """
    print("\033[37m")
    print("This program will convert from binary to text and vice versa.\n")
    print("Enter '1' to convert from binary to text.")
    print("Enter '2' to convert from text to binary.")
    print("At any time, press ^C to exit.\n")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                binary = input("Enter your binary string: ")
                print(binary_to_text(binary))
        elif choice == "2":
            while True:
                text = input("Enter your text string: ")
                print(text_to_binary(text))
        else:
            print("\033[31mInvalid choice.")
            print("Exiting...")
            exit()

while True:
    main()