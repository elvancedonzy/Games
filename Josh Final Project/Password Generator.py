#Importing the relevant modules
import time
import qrcode
from random import randint

#All uppercase password
password = ""
for i in range(4):
  i = chr(randint(65, 90))
#Adds lower case
  for j in range(4):
    j = chr(randint(65, 90)).lower()
#Adds numbers 
    for k in range(3):
      k = randint(0, 10)
  password = str(password) + i + j + str(k)
print(password)

#  -------------> Second Part of project <----------------
#Incode the password and turn it to a qrcode 
img =qrcode.make(password)
img.save("password.jpg")


# Sleep for 10 seconds
time.sleep(10)