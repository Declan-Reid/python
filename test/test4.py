import os

command = 'rm -rf ~/Desktop/test.txt'
p = os.system('echo %s' % (command))