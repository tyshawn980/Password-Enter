#Coded by Tyshawn Rene
#PasswordEnterer
#Takes a list with passwords in it and enters it into a username field, password field, and logs in


#importing modules
import time
from ppadb.client import Client as AdbClient

#Connecting the device
def connect():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

#Prompting a txt file to read from
filename = input("What is the path to your password file?")
with open(filename) as file:
  filelen = len(file.readlines())#getting the length of the password directory
file.close()

with open(filename) as file1:
  file2 = [line.rstrip('\n') for line in file1]
#Executing the inputs
username = input("What is the username you want to use?")
if __name__ == '__main__':
    device, client = connect()
    username_coords = '153 995'
    password = '150 1181'
    password2 = '164 1153 164 1153 2000' #has 5 coordinates because it is a swipe that starts and ends at the same place, therefore turning it into a long press on the phone screen
    deletebutton= '984 1916'
    login = '529 1300'

device.shell(f'input tap "{username_coords}"')
time.sleep(0.5)
device.shell(f'input text {username}')
time.sleep(0.5)
device.shell(f'input tap {password}')
time.sleep(0.5)

#Loop for inputting password from current index in list and pressing login. It also displays the current index.
ct = 0
x = 0 #variable keeps track of which line in the passlist to type
while ct < filelen:
  device.shell(f'input text "{file2[x]}"')
  time.sleep(0.5)
  device.shell(f'input tap {login}')
  time.sleep(10)
  device.shell(f'input swipe {password2}')
  time.sleep(1.5)
  device.shell(f'input tap {deletebutton}')
  print(file2[x])
  ct += 1
  x += 1


print ("The program is finished.")