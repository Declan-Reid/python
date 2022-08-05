#!/usr/bin/env python3
import sys
import os
try:
    print()
    print('CC: Compiling '+sys.argv[1]+'.cpp to '+sys.argv[1]+'.')
    result = os.system('g++ -o '+sys.argv[1]+' '+sys.argv[1]+'.cpp')
    if result == 0:
        print('CC: Compiled Successfully. Formatting and Running...')
        os.system('chmod +x '+sys.argv[1])
        print('CC: ==============================')
        os.system('./'+sys.argv[1])
        print('CC: ==============================')
        print('CC: Run Successfully.\n')
    else:
        print('CC: Compilation Failed.')
        print('CC: Error logs above.\n')
except IndexError:
    print('CC: Usage: g <filename>\n')
    sys.exit(1)
except FileNotFoundError:
    print('CC: File not found\n')
    sys.exit(1)
except:
    print('ErCCror: Unknown error\n')
    sys.exit(1)