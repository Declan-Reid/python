global number

while True:
    number = int()
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")

    binary = ''
    
    if number > 127:
        binary = binary + '1'
        number = number - 128
    else:
        binary = binary + '0'

    if number > 63:
        binary = binary + '1'
        number = number - 64
    else:
        binary = binary + '0'

    if number > 31:
        binary = binary + '1'
        number = number - 32
    else:
        binary = binary + '0'

    if number > 15:
        binary = binary + '1'
        number = number - 16
    else:
        binary = binary + '0'

    if number > 7:
        binary = binary + '1'
        number = number - 8
    else:
        binary = binary + '0'

    if number > 3:
        binary = binary + '1'
        number = number - 4
    else:
        binary = binary + '0'

    if number > 1:
        binary = binary + '1'
        number = number - 2
    else:
        binary = binary + '0'

    if number > 0:
        binary = binary + '1'
        number = number - 1
    else:
        binary = binary + '0'

    if number > 0:
        binary = binary + ' | with remainder ' + str(number)

    print('Binary equivilent: '+binary)
    print()