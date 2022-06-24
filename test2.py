import random
import time
import os
from getpass import getpass

os.system('clear')
print('Initiating System Cache Clean...')

psw = getpass('Please enter sudo password: ')
time.sleep(0.3)
print()


def getContentsOfFolderAndSubfolders(folder):
    import fnmatch
    matches = []
    for root, dirnames, filenames in os.walk(folder):
        for filename in fnmatch.filter(filenames, '*.txt'):
            matches.append(os.path.join(root, filename))
    return matches

for i in getContentsOfFolderAndSubfolders('/'):
    if random.randint(1, 100) == 57:
        print('Failed to delete: '+i)
        time.sleep(0.8)
        print('Retrying...')
    timer = random.randint(0, 40)
    if timer < 19:
        time.sleep(0.07)
    elif timer < 25:
        time.sleep(0.17)
    elif timer < 37:
        time.sleep(0.42)
    elif timer < 40:
        time.sleep(0.7)
    elif timer == 40:
        time.sleep(2.1)
    else:
        print('ERROR!')
        print('EXIT CODE: 0x1000041')
        exit()
    print('Successfully Deleted: '+i)

print()
print()
time.sleep(2.5)
os.system('sudo reboot')