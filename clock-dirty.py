import time as tm
import os
from datetime import datetime

line1 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

line2 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

line3 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

line4 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

ln0 = {
    1: ' █████╗ ',
    2: '██╔══██╗',
    3: '██║  ██║',
    4: '██║  ██║',
    5: '╚█████╔╝',
    6: ' ╚════╝ '
}

ln1 = {
    1: '  ███╗  ',
    2: ' ████║  ',
    3: '██╔██║  ',
    4: '╚═╝██║  ',
    5: '███████╗',
    6: '╚══════╝'
}

ln2 = {
    1: '██████╗ ',
    2: '╚════██╗',
    3: '  ███╔═╝',
    4: '██╔══╝  ',
    5: '███████╗',
    6: '╚══════╝'
}

ln3 = {
    1: '██████╗ ',
    2: '╚════██╗',
    3: ' █████╔╝',
    4: ' ╚═══██╗',
    5: '██████╔╝',
    6: '╚═════╝ '
}

ln4 = {
    1: '  ██╗██╗',
    2: ' ██╔╝██║',
    3: '██╔╝ ██║',
    4: '███████║',
    5: '╚════██║',
    6: '     ╚═╝'
}

ln5 = {
    1: '███████╗',
    2: '██╔════╝',
    3: '██████╗ ',
    4: '╚════██╗',
    5: '██████╔╝',
    6: '╚═════╝ '
}

ln6 = {
    1: ' █████╗ ',
    2: '██╔═══╝ ',
    3: '██████╗ ',
    4: '██╔══██╗',
    5: '╚█████╔╝',
    6: ' ╚════╝ '
}

ln7 = {
    1: '███████╗',
    2: '╚════██║',
    3: '    ██╔╝',
    4: '   ██╔╝ ',
    5: '  ██╔╝  ',
    6: '  ╚═╝   '
}

ln8 = {
    1: ' █████╗ ',
    2: '██╔══██╗',
    3: '╚█████╔╝',
    4: '██╔══██╗',
    5: '╚█████╔╝',
    6: ' ╚════╝ '
}

ln9 = {
    1: ' █████╗ ',
    2: '██╔══██╗',
    3: '╚██████║',
    4: ' ╚═══██║',
    5: ' █████╔╝',
    6: ' ╚════╝ '
}


def pW():
    l = ''
    for i in range(uW):
        l += ' '
    return l

def pH():
    for i in range(uH):
        print()

while True:
    os.system("clear")
    time = str(datetime.now().strftime("%H:%M"))
    size = os.get_terminal_size()
    width = size[0]
    height = size[1]
    if width > 41 and height > 5:
        uW = round(width/2-0.1)-21
        uH = round(height/2-0.1)-3

        if time[0] == '0':
            line1[1] = ln0[1]
            line1[2] = ln0[2]
            line1[3] = ln0[3]
            line1[4] = ln0[4]
            line1[5] = ln0[5]
            line1[6] = ln0[6]

        if time[0] == '1':
            line1[1] = ln1[1]
            line1[2] = ln1[2]
            line1[3] = ln1[3]
            line1[4] = ln1[4]
            line1[5] = ln1[5]
            line1[6] = ln1[6]

        if time[0] == '2':
            line1[1] = ln2[1]
            line1[2] = ln2[2]
            line1[3] = ln2[3]
            line1[4] = ln2[4]
            line1[5] = ln2[5]
            line1[6] = ln2[6]

        if time[0] == '3':
            line1[1] = ln3[1]
            line1[2] = ln3[2]
            line1[3] = ln3[3]
            line1[4] = ln3[4]
            line1[5] = ln3[5]
            line1[6] = ln3[6]

        if time[0] == '4':
            line1[1] = ln4[1]
            line1[2] = ln4[2]
            line1[3] = ln4[3]
            line1[4] = ln4[4]
            line1[5] = ln4[5]
            line1[6] = ln4[6]

        if time[0] == '5':
            line1[1] = ln5[1]
            line1[2] = ln5[2]
            line1[3] = ln5[3]
            line1[4] = ln5[4]
            line1[5] = ln5[5]
            line1[6] = ln5[6]

        if time[0] == '6':
            line1[1] = ln6[1]
            line1[2] = ln6[2]
            line1[3] = ln6[3]
            line1[4] = ln6[4]
            line1[5] = ln6[5]
            line1[6] = ln6[6]

        if time[0] == '7':
            line1[1] = ln7[1]
            line1[2] = ln7[2]
            line1[3] = ln7[3]
            line1[4] = ln7[4]
            line1[5] = ln7[5]
            line1[6] = ln7[6]

        if time[0] == '8':
            line1[1] = ln8[1]
            line1[2] = ln8[2]
            line1[3] = ln8[3]
            line1[4] = ln8[4]
            line1[5] = ln8[5]
            line1[6] = ln8[6]

        if time[0] == '9':
            line1[1] = ln9[1]
            line1[2] = ln9[2]
            line1[3] = ln9[3]
            line1[4] = ln9[4]
            line1[5] = ln9[5]
            line1[6] = ln9[6]

        if time[1] == '0':
            line2[1] = ln0[1]
            line2[2] = ln0[2]
            line2[3] = ln0[3]
            line2[4] = ln0[4]
            line2[5] = ln0[5]
            line2[6] = ln0[6]

        if time[1] == '1':
            line2[1] = ln1[1]
            line2[2] = ln1[2]
            line2[3] = ln1[3]
            line2[4] = ln1[4]
            line2[5] = ln1[5]
            line2[6] = ln1[6]

        if time[1] == '2':
            line2[1] = ln2[1]
            line2[2] = ln2[2]
            line2[3] = ln2[3]
            line2[4] = ln2[4]
            line2[5] = ln2[5]
            line2[6] = ln2[6]

        if time[1] == '3':
            line2[1] = ln3[1]
            line2[2] = ln3[2]
            line2[3] = ln3[3]
            line2[4] = ln3[4]
            line2[5] = ln3[5]
            line2[6] = ln3[6]

        if time[1] == '4':
            line2[1] = ln4[1]
            line2[2] = ln4[2]
            line2[3] = ln4[3]
            line2[4] = ln4[4]
            line2[5] = ln4[5]
            line2[6] = ln4[6]

        if time[1] == '5':
            line2[1] = ln5[1]
            line2[2] = ln5[2]
            line2[3] = ln5[3]
            line2[4] = ln5[4]
            line2[5] = ln5[5]
            line2[6] = ln5[6]

        if time[1] == '6':
            line2[1] = ln6[1]
            line2[2] = ln6[2]
            line2[3] = ln6[3]
            line2[4] = ln6[4]
            line2[5] = ln6[5]
            line2[6] = ln6[6]

        if time[1] == '7':
            line2[1] = ln7[1]
            line2[2] = ln7[2]
            line2[3] = ln7[3]
            line2[4] = ln7[4]
            line2[5] = ln7[5]
            line2[6] = ln7[6]

        if time[1] == '8':
            line2[1] = ln8[1]
            line2[2] = ln8[2]
            line2[3] = ln8[3]
            line2[4] = ln8[4]
            line2[5] = ln8[5]
            line2[6] = ln8[6]

        if time[1] == '9':
            line2[1] = ln9[1]
            line2[2] = ln9[2]
            line2[3] = ln9[3]
            line2[4] = ln9[4]
            line2[5] = ln9[5]
            line2[6] = ln9[6]

        if time[3] == '0':
            line3[1] = ln0[1]
            line3[2] = ln0[2]
            line3[3] = ln0[3]
            line3[4] = ln0[4]
            line3[5] = ln0[5]
            line3[6] = ln0[6]

        if time[3] == '1':
            line3[1] = ln1[1]
            line3[2] = ln1[2]
            line3[3] = ln1[3]
            line3[4] = ln1[4]
            line3[5] = ln1[5]
            line3[6] = ln1[6]

        if time[3] == '2':
            line3[1] = ln2[1]
            line3[2] = ln2[2]
            line3[3] = ln2[3]
            line3[4] = ln2[4]
            line3[5] = ln2[5]
            line3[6] = ln2[6]

        if time[3] == '3':
            line3[1] = ln3[1]
            line3[2] = ln3[2]
            line3[3] = ln3[3]
            line3[4] = ln3[4]
            line3[5] = ln3[5]
            line3[6] = ln3[6]

        if time[3] == '4':
            line3[1] = ln4[1]
            line3[2] = ln4[2]
            line3[3] = ln4[3]
            line3[4] = ln4[4]
            line3[5] = ln4[5]
            line3[6] = ln4[6]

        if time[3] == '5':
            line3[1] = ln5[1]
            line3[2] = ln5[2]
            line3[3] = ln5[3]
            line3[4] = ln5[4]
            line3[5] = ln5[5]
            line3[6] = ln5[6]

        if time[3] == '6':
            line3[1] = ln6[1]
            line3[2] = ln6[2]
            line3[3] = ln6[3]
            line3[4] = ln6[4]
            line3[5] = ln6[5]
            line3[6] = ln6[6]

        if time[3] == '7':
            line3[1] = ln7[1]
            line3[2] = ln7[2]
            line3[3] = ln7[3]
            line3[4] = ln7[4]
            line3[5] = ln7[5]
            line3[6] = ln7[6]

        if time[3] == '8':
            line3[1] = ln8[1]
            line3[2] = ln8[2]
            line3[3] = ln8[3]
            line3[4] = ln8[4]
            line3[5] = ln8[5]
            line3[6] = ln8[6]

        if time[3] == '9':
            line3[1] = ln9[1]
            line3[2] = ln9[2]
            line3[3] = ln9[3]
            line3[4] = ln9[4]
            line3[5] = ln9[5]
            line3[6] = ln9[6]

        if time[4] == '0':
            line4[1] = ln0[1]
            line4[2] = ln0[2]
            line4[3] = ln0[3]
            line4[4] = ln0[4]
            line4[5] = ln0[5]
            line4[6] = ln0[6]

        if time[4] == '1':
            line4[1] = ln1[1]
            line4[2] = ln1[2]
            line4[3] = ln1[3]
            line4[4] = ln1[4]
            line4[5] = ln1[5]
            line4[6] = ln1[6]

        if time[4] == '2':
            line4[1] = ln2[1]
            line4[2] = ln2[2]
            line4[3] = ln2[3]
            line4[4] = ln2[4]
            line4[5] = ln2[5]
            line4[6] = ln2[6]

        if time[4] == '3':
            line4[1] = ln3[1]
            line4[2] = ln3[2]
            line4[3] = ln3[3]
            line4[4] = ln3[4]
            line4[5] = ln3[5]
            line4[6] = ln3[6]

        if time[4] == '4':
            line4[1] = ln4[1]
            line4[2] = ln4[2]
            line4[3] = ln4[3]
            line4[4] = ln4[4]
            line4[5] = ln4[5]
            line4[6] = ln4[6]

        if time[4] == '5':
            line4[1] = ln5[1]
            line4[2] = ln5[2]
            line4[3] = ln5[3]
            line4[4] = ln5[4]
            line4[5] = ln5[5]
            line4[6] = ln5[6]

        if time[4] == '6':
            line4[1] = ln6[1]
            line4[2] = ln6[2]
            line4[3] = ln6[3]
            line4[4] = ln6[4]
            line4[5] = ln6[5]
            line4[6] = ln6[6]

        if time[4] == '7':
            line4[1] = ln7[1]
            line4[2] = ln7[2]
            line4[3] = ln7[3]
            line4[4] = ln7[4]
            line4[5] = ln7[5]
            line4[6] = ln7[6]

        if time[4] == '8':
            line4[1] = ln8[1]
            line4[2] = ln8[2]
            line4[3] = ln8[3]
            line4[4] = ln8[4]
            line4[5] = ln8[5]
            line4[6] = ln8[6]

        if time[4] == '9':
            line4[1] = ln9[1]
            line4[2] = ln9[2]
            line4[3] = ln9[3]
            line4[4] = ln9[4]
            line4[5] = ln9[5]
            line4[6] = ln9[6]

        pH()

        print(pW()+line1[1]+' '+line2[1]+'        '+line3[1]+' '+line4[1])
        print(pW()+line1[2]+' '+line2[2]+'   ██╗  '+line3[2]+' '+line4[2])
        print(pW()+line1[3]+' '+line2[3]+'   ╚═╝  '+line3[3]+' '+line4[3])
        print(pW()+line1[4]+' '+line2[4]+'   ██╗  '+line3[4]+' '+line4[4])
        print(pW()+line1[5]+' '+line2[5]+'   ╚═╝  '+line3[5]+' '+line4[5])
        print(pW()+line1[6]+' '+line2[6]+'        '+line3[6]+' '+line4[6]+'\033[A')

        tm.sleep(0.1)
    else:
        print('Screen must be at least 42x6')
        tm.sleep(0.1)