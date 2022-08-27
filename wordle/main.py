import pathlib
import socket

list = open(str(pathlib.Path(__file__).parent.resolve())+'/words.txt', 'r').read()

print(list)