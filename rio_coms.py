#v Imports/variables v#
import string
import board
import serial
rio = serial.Serial('/dev/serial0', 9600, timeout = 0, write_timeout = 0)
#usb is dev/serial1
#checks if the robot has been disabled
def disabled():
    standin = rio.read().decode('utf-8')
    if standin == 'D':
        return True
    else:
        return False

def loop():
    rio.write('D'.encode('utf-8'))
    

#def disabled():
#    print((rio.read()).decode('utf-8'))
#    if rio.read() is 'D':                  #This block can be renamed and use a different byte for any command from the rio
#        return True
#    else:
#        return False


#sends values to rio and prints them, add any new sensors to this
def send_value(laser, value):
    
    print("Laser {}: {}".format(laser, value))
    rio.write(value)
    
def test_send(value):
    if rio.isOpen():
        pass
    else: 
        rio.open()
    print(f"So help me god this had better work: {value}")
    rio.write(str(value).encode("utf-8"))

def test_read():
    rioOut = rio.read()
    # rioString = rioOut.decode('utf-8')
    print(rioOut)