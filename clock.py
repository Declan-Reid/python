#!/usr/bin/env python3
import time as tm
import os
from datetime import datetime
import sys

oldTime = '00:00'
oldWidth = 0
oldHeight = 0
initial = True

place1 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

place2 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

place3 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

place4 = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: ''
}

lin1 = {
    0: ' █████╗ ',
    1: '  ███╗  ',
    2: '██████╗ ',
    3: '██████╗ ',
    4: '  ██╗██╗',
    5: '███████╗',
    6: ' █████╗ ',
    7: '███████╗',
    8: ' █████╗ ',
    9: ' █████╗ '
}

lin2 = {
    0: '██╔══██╗',
    1: ' ████║  ',
    2: '╚════██╗',
    3: '╚════██╗',
    4: ' ██╔╝██║',
    5: '██╔════╝',
    6: '██╔═══╝ ',
    7: '╚════██║',
    8: '██╔══██╗',
    9: '██╔══██╗'
}

lin3 = {
    0: '██║  ██║',
    1: '██╔██║  ',
    2: '  ███╔═╝',
    3: ' █████╔╝',
    4: '██╔╝ ██║',
    5: '██████╗ ',
    6: '██████╗ ',
    7: '    ██╔╝',
    8: '╚█████╔╝',
    9: '╚██████║'
}

lin4 = {
    0: '██║  ██║',
    1: '╚═╝██║  ',
    2: '██╔══╝  ',
    3: ' ╚═══██╗',
    4: '███████║',
    5: '╚════██╗',
    6: '██╔══██╗',
    7: '   ██╔╝ ',
    8: '██╔══██╗',
    9: ' ╚═══██║'
}

lin5 = {
    0: '╚█████╔╝',
    1: '███████╗',
    2: '███████╗',
    3: '██████╔╝',
    4: '╚════██║',
    5: '██████╔╝',
    6: '╚█████╔╝',
    7: '  ██╔╝  ',
    8: '╚█████╔╝',
    9: ' █████╔╝'
}

lin6 = {
    0: ' ╚════╝ ',
    1: '╚══════╝',
    2: '╚══════╝',
    3: '╚═════╝ ',
    4: '     ╚═╝',
    5: '╚═════╝ ',
    6: ' ╚════╝ ',
    7: '  ╚═╝   ',
    8: ' ╚════╝ ',
    9: ' ╚════╝ '
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
    try:
        time = str(datetime.now().strftime("%H:%M"))
        size = os.get_terminal_size()
        width = size[0]
        height = size[1]
        uH = int(round(height/2-3.1))
        uW = int(round(width/2-21.1))
        if oldTime != time or oldWidth != width or oldHeight != height or initial == True:
            os.system("clear")
            oldTime = time
            oldWidth = width
            oldHeight = height
            if width > 41 and height > 5:
                uW = round(width/2-0.1)-21
                uH = round(height/2-0.1)-3

                place1[1] = lin1[int(time[0])]
                place1[2] = lin2[int(time[0])]
                place1[3] = lin3[int(time[0])]
                place1[4] = lin4[int(time[0])]
                place1[5] = lin5[int(time[0])]
                place1[6] = lin6[int(time[0])]

                place2[1] = lin1[int(time[1])]
                place2[2] = lin2[int(time[1])]
                place2[3] = lin3[int(time[1])]
                place2[4] = lin4[int(time[1])]
                place2[5] = lin5[int(time[1])]
                place2[6] = lin6[int(time[1])]

                place3[1] = lin1[int(time[3])]
                place3[2] = lin2[int(time[3])]
                place3[3] = lin3[int(time[3])]
                place3[4] = lin4[int(time[3])]
                place3[5] = lin5[int(time[3])]
                place3[6] = lin6[int(time[3])]

                place4[1] = lin1[int(time[4])]
                place4[2] = lin2[int(time[4])]
                place4[3] = lin3[int(time[4])]
                place4[4] = lin4[int(time[4])]
                place4[5] = lin5[int(time[4])]
                place4[6] = lin6[int(time[4])]

                pH()

                print(pW()+place1[1]+' '+place2[1]+'        '+place3[1]+' '+place4[1])
                print(pW()+place1[2]+' '+place2[2]+'   ██╗  '+place3[2]+' '+place4[2])
                print(pW()+place1[3]+' '+place2[3]+'   ╚═╝  '+place3[3]+' '+place4[3])
                print(pW()+place1[4]+' '+place2[4]+'   ██╗  '+place3[4]+' '+place4[4])
                print(pW()+place1[5]+' '+place2[5]+'   ╚═╝  '+place3[5]+' '+place4[5])
                print(pW()+place1[6]+' '+place2[6]+'        '+place3[6]+' '+place4[6]+'\033[A')

                tm.sleep(0.1)
                initial = False
            else:
                print('Screen must be')
                print('at least 42x6')
                initial = True
                tm.sleep(0.1)
            
    except Exception as e:
        print(e)
        sys.exit()