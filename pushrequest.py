import pyfcm
from pyfcm import  errors
import json

def push():
    with open('./status.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    push_service = pyfcm.FCMNotification(api_key='AAAAmKROC5Y:APA91bEi-2ni1Qz4kWrIPGf5WGnkUU4E4ZLJQ_O_HFqLl3SRuTcXuMyM4-ajlETZ4gXFe6OqPov6dvrpCNBYOkss5a022I6bEfImBNnQYKabtJ0QJCi4LHzQl4WLWXskqaqoqzAPdEkr')
    print(json_data['token'])
    try:
        response = push_service.notify_single_device(registration_id=json_data['token'],
                                                  message_title='화재발생',
                                                  message_body='화재가 발생하였습니다. 대피 바랍니다.')
    except errors.InvalidDataError:
        print("error:push invalid data")
        return None
    else:
        return response