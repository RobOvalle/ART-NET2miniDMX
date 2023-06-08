import serial, time
from stupidArtnet import StupidArtnetServer
import keyboard
import binascii

import yaml
config = yaml.safe_load(open("config.yml"))

DMXpacket = bytearray(513)

def test_callback(data):
    for i in range(512):
        DMXpacket[i] = data[i]
        
        
universe = config['artnet']['universo']
net = config['artnet']['ip']
a = StupidArtnetServer()  
u1_listener = a.register_listener(
    universe, callback_function=test_callback)   
        
puerto = config['dispositivo']['puerto']
arduino = serial.Serial(puerto, 115200)
print('ARTnet a COM')
print('Saliendo desde')
print(net)
print('unvierso')
print(universe)
print('a la interfaz en')
print(puerto)


while True:
    time.sleep(0.040)
    #print('ARTnet a COM')
    #print(DMXpacket)
    #recibe artnet
    #envia COM
    arduino.write(binascii.a2b_hex('5A'))
    arduino.write(binascii.a2b_hex('A2'))
    arduino.write(DMXpacket)
    arduino.write(binascii.a2b_hex('A5'))

    if keyboard.is_pressed('esc'):
        a.close();
        arduino.close()
        del a
        del arduino
        break
