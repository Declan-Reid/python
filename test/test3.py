import random
import time

text = '0'

while True:
    print(text)
    for i in range(len(str(text))):
        text += str(random.randint(0, 1))
    time.sleep(0.5)