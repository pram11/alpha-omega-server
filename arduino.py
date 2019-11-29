import serial
import time
import json


ser = serial.Serial(
    port="COM7",
    baudrate=9600
)
while True:
    print("status checking...")
    with open('./status.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    print(json_data['status'])
    if json_data['status']=='fire':
        ser.write('f'.encode())
        print(ser.readline())
    elif json_data['status']=='normal':
        ser.write('n'.encode())
        print(ser.readline())
    time.sleep(2)
