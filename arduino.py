import serial
import time
import json


ser = serial.Serial(
    port="COM3",
    baudrate=9600
)
while True:
    print("status checking start")
    with open('./status.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    print(json_data['status'])
    if json_data['status']=='fire':
        ser.write('status:fire\n'.encode())
        print(ser.readline())
    elif json_data['status']=='normal':
        ser.write('status:normal\n'.encode())
        print(ser.readline())
    val=''
    val = ser.readline()
    print(val)
    print("turn end!")
    time.sleep(2)
