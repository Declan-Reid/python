
b1 = "01000100 01100001 01101110 01101001 00100000 01101001 01110011"
b2 = "00100000 01100011 01101111 01101111 01101100 00101110"
binary = b1+b2

text = ""
binary = binary.replace(" ", "")
for i in range(0, len(binary), 8):
    text += chr(int(binary[i:i+8], 2))

print(text)

