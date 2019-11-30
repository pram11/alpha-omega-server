import serial
import time
import json
import pushrequest

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
    timeout=2
)
status = 'normal'
val=''
#signal_from {server,arduino,none}
singal_from = 'none'


while True:
    print("status checking start")
    with open('./status.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    print("file_status:"+json_data['status'])
    print("status:"+status)
    if not status == json_data['status']:
        print("status")
        if json_data['status']=='fire':
            ser.write('server:fire\n'.encode())
        elif json_data['status']=='normal':
            ser.write('server:normal\n'.encode())
        print(ser.readline())
        status = json_data['status']
    val = ser.readline()

    print(val.decode())
    if (val.decode()=="arduino:fire\r\n"):
        json_data['status']='fire'
        pushrequest.push()
        with open('./status.json','w',encoding='utf-8') as js_w:
            json.dump(json_data,js_w)
        status='fire'
    print("turn end!")
