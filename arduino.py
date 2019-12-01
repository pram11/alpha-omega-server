import serial
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
escaped_status = False
push_initial = True

while True:
    print("status checking start")
    #status 파일 읽음
    with open('./status.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    if escaped_status != json_data['is_escaped']:
        if json_data['is_escaped'] == True:
            print("server:escaped")
            ser.write('server:escaped\n'.encode())
            escaped_status = json_data['is_escaped']
        if json_data['is_escaped']==False:
            print("set escaped data initialize")
            escaped_status = False

    if not status == json_data['status']:
    #json 파일 내의 상태가 status 변수의 상태와 다를때
        print("status")
        #화재일경우
        if json_data['status']=='fire':
            print("server:fire")
            ser.write('server:fire\n'.encode())
        #아두이노에 server:fire 보냄
        elif json_data['status']=='normal':
            print("server:normal")
            ser.write('server:normal\n'.encode())
        #아두이노에 server:normal 보냄
        status = json_data['status']
        #파일에 맞춤
    try:
        val = ser.readline()
    except serial.SerialException:
        print("serial exception occured")
    print(val)
    print("arduino:fire\r\n".encode())
    if (val.decode()=="arduino:fire"):
        print("fire on arduino")
        pushrequest.push()
        json_data['status']='fire'
        token = json_data['token']
        json_data['token']=token
        with open('./status.json','w',encoding='utf-8') as js_w:
            json.dump(json_data,js_w)
        status='fire'
    print("turn end!")


