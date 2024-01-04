import base64

# Opening the file which contains all the encoded names

f = open("attendance.txt")
byte_strings = f.readlines()

#print([i.replace("\n","") for i in list(set(byte_strings))])

byte_strings = [i.replace("\n","") for i in list(set(byte_strings))]

# Decode and print the decoded strings
for byte_string in byte_strings:
    decoded_data = base64.b64decode(byte_string[3:-1]).decode('utf-8')
    print(decoded_data)
