import vk
import time
import datetime
import p
import par
import requests

print('VKBot');
session = vk.Session('b380f3223d6ef3753924849a8f69633ed076fa338f40a386c8ee0e852e64c13f1189ff4766bafc4b4dbc8');

api = vk.API(session)

messages = api.messages.get();

#print(messages)
commands = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
trans_day = {'понедельник':'monday','вторник':'tuesday','среда':'wednesday','четверг':'thursday','пятница':'friday',
                'суббота':'saturday','воскресенье':'sunday'}
keywords = ['нижняя', 'верхняя']


#pavlikyv
def pos_day(txt):
    return next(command for command in commands if command in txt)

while (True):
    messages = api.messages.get();

    for m in messages[1:]:
        if m['read_state'] == 0:

            # Если сообщение не прочитано
            if m['read_state'] == 0:

                # id сообщения
                uid = m['uid']
                uid2 = uid
                #user_first_name = api.users.get(user_ids=uid)[0]['first_name']

                try:
                    # id чата
                    chat_id = m['chat_id']
                except:
                    chat_id = 0
                    user_last_name = api.users.get(user_ids=uid)[0]['last_name']

                if chat_id > 0:
                    uid = 0




                # Форматированный текст сообщения
                text = m['body'].lower()
                text = text.replace(' ', '')

                date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

                if text == 'help':
                    api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n'+ '\nCommands🙏:\n1. Погода в [город]\n2. Где пара'
                                                                                '\n3. Какая неделя'
                                                                                '\n4. Какие пары\n5. Пары завтра\n6.[какая неделя] [какой день]' )

                if text[0:7:1] == "погодав":
                    api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n'+p.weather_now(text))


                for keyword in ['нижняя', 'верхняя']:
                    if keyword in text:
                        change_day = next(c for c in commands if c in text)
                        if change_day != None:
                             api.messages.send(uid=uid, chat_id=chat_id,
                                          message=date_time_string + '\n' + par.para_per_day(keyword,
                                                                                             trans_day[change_day]))
                        break


                if text == 'гдепара' or text == 'гдесейчаспара':
                   api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n' + par.Gde_para(datetime.datetime.now()))
                if text == "какаянеделя" or  text == "какаясейчаснеделя" or  text == "какаяэтонеделя":
                    api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n Сейчас ' + par.Week_name(datetime.datetime.now()))
                if text == "какиепары" or text == "какиесегодняпары" or text == "чезапары":
                    api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n  '
                                        + par.Week_name(datetime.datetime.now())+ ',  '+par.Kakoy_den()+ '\n '+ par.UPweek_Show(datetime.datetime.now().strftime('%A').lower()))
                if text == "парызавтра" or text == "какиепарызавтра" or text == "какиезавтрапары":
                    api.messages.send(uid=uid, chat_id=chat_id, message=date_time_string + '\n'+
                                        par.Day_next())
                    #print(text[0:7:1])
    api.messages.markAsRead(message_ids=m['mid'])
    time.sleep(3);




