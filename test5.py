import os
def compare_strings(a, b):
    os.system('clear')
    if a is None or b is None:
        print("Number of Same Characters: 0")
        return
    
    size = min(len(a), len(b)) # Finding the minimum length
    count = 0 # A counter to keep track of same characters
    used = 0

    for i in range(size):
        if a[i] == b[i]:
            count += 1 # Updating the counter when characters are same at an index
        else:
            if used != 1:
                print('Decimal of pi:', count-2)
                used = 1

    if used != 1:
        print("Decimals of pi:", count-2)

while True:
    print()
    compare_strings(input('Enter: '), '3.141592653589793238462643383279')
    print()