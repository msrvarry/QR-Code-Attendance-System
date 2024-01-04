import cv2
from pyzbar.pyzbar import decode
import time

#starting the webcam
cap = cv2.VideoCapture(0)
names = []

#function for attendance file
fob = open('attendance.txt' , 'a+')

def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = "".join(str(z))
        fob.write(z + "\n")
        return names

print("Reading the scanned QR code....")

#function data present or not
def checkData(data):
    data = str(data)
    if data in names:
        print("You have already been marked present..")
    else:
        print('\n'+str(len(names)+1)+'\n'+'You have been marked present')
        enterData(data)

while True:
    _ , frame = cap.read()
    decodeObject = decode(frame)
    for obj in decodeObject:
        checkData(obj.data)
        print("Your roll number: ",obj.data)
        time.sleep(1)
    cv2.imshow('Frame', frame)

    #closing the webcam
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()