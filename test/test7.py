import os

try:
    workingDirectory = os.getcwd()
    fileDirectory = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        print('Working Directory: ' + workingDirectory)
        print('File Directory: ' + fileDirectory)
except (SystemExit or KeyboardInterrupt):
    print('Ok boomer')
    print()