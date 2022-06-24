# Import libraries
import json
import os.path
import time
import os

# Makes variables global
global fileName
fileName = ''
global file_exists
file_exists = ''

# Get file name and check if it already exists
fileName = input('File Name : ')
os.system('clear')
# Check if file ends with .json

if len(fileName) > 5:
    if fileName[-5]+fileName[-4]+fileName[-3]+fileName[-2]+fileName[-1] != '.json':
        fileName = fileName+'.json'
else:
    fileName = fileName+'.json'

try:
    file_exists = os.path.exists(fileName)
except FileNotFoundError:
    file_exists = False

if file_exists == True:
    # Opens file
    f = open(fileName)
elif file_exists == False:
    fw = open(fileName, 'x')
    fw.write('{')
    fw.write('\n')
    fw.write('    "History": [')
    fw.write('\n')
    fw.write('        {')
    fw.write('\n')
    fw.write('            "Username": "Server",')
    fw.write('\n')
    fw.write('            "Message": "Initial Creation"')
    fw.write('\n')
    fw.write('        }')
    fw.write('\n')
    fw.write('    ]')
    fw.write('\n')
    fw.write('}')
    fw.write('\n')
    fw.close()
    f = open(fileName)
else:
    print('An unexpected error has occured opening your file. (Error code: 1)')
    exit()

# Returns JSON object as a dictionary
data = json.load(f)
fw = open(fileName, 'w')

# Iterating through the json list
for i in data["History"]:
    if i["Username"] == 'Server':
        print('\033[1;31m'+i["Username"]+':'+'\n'+'\033[1;36m'+i["Message"]+'\n')
    else:
        print('\033[31m'+i["Username"]+':'+'\n'+'\033[36m'+i["Message"]+'\n')
  
# Closing file
f.close()