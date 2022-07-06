import itertools
import time

sourceFile = open('character-output.txt', 'w')
lil = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', ';', "'", ',', '.', '/', '{', '}', '|', ':', '"', '<', '>', '?', '`', '~']
lim = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
startChr = int(input('How many characters do you want to start with? '))
endChr = int(input('How many characters do you want to end with? '))
charType = input('What length of characters do you want to use? (lil = long, lim = medium, lis = short) ')
if charType == 'lil':
    charType = lil
elif charType == 'lim':
    charType = lim
elif charType == 'lis':
    charType = lis
else:
    print('Invalid input')
    exit()
characters = 0

for i in range(startChr):
    characters += 1
    print(characters)
    time.sleep(0.5)

def foo(l):
    yield from itertools.product(*([l] * characters)) 

while characters < endChr:
    for x in foo(charType):
        print(''.join(x), file = sourceFile)
        time.sleep(0.1)
    if len(characters) < endChr:
        characters += 'a'
    else:
        break

if characters == endChr:
    for x in foo(charType):
        print(''.join(x), file = sourceFile)