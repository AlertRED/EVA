import datetime

def Week_name(d):
    days = int((d+datetime.timedelta(days=3)).strftime('%j'))
    if  ((days // 7) % 2) == 0:
         return 'Нижняя неделя'
    else:
         return 'Верхняя неделя'

translate_day = {'monday':'понедельник','tuesday':'вторник','wednesday':'среда','thursday':'четверг',
                 'friday':'пятница','saturday':'суббота','sunday':'воскресенье'}

name_urok = ['лаб.Машинно зависимые ЯП','лек.Машинно зависимые ЯП','лаб.Физика','пр.Физика','лек.Физика',
             'пр.Мат. Логика','лек.Мат. Логика','лек.физра','секц.физра','пр.Теор.вер','лек.Теор.вер',
             'лаб.Основы программирования','лек.Основы программирования','Православная культура',
             'лек.Философия','пр.Философия']

aud_up_week =[['2-305','433','3-107','+'],
                ['-','-','-','-','-'],
                ['-','-','-','-','-'],
                ['-','-','8-431','384','438'],
                ['313','4-106','спортзал','-','-'],
                ['490','4-206','8-406','-','-']]

aud_low_week =[['-','433','8-109','-'],
                ['490','2-305','-','-','-'],
                ['-','109','спортзал','8-507','-'],
                ['282','184а','109','109','-'],
                ['-','-','спортзал','-','-'],
                ['490','358','3-202','-','-']]

up_week = [[name_urok[0],name_urok[2],name_urok[5],name_urok[7]],
           ['Пусто','Пусто','Пусто','Пусто','Пусто'],
           ['Пусто','Пусто','Пусто','Пусто','Пусто'],
           ['Пусто','Пусто',name_urok[9],name_urok[4],name_urok[3]],
           [name_urok[10],name_urok[11],name_urok[7],'Пусто','Пусто'],
           [name_urok[12],name_urok[15],name_urok[14],'Пусто','Пусто']]

low_week = [['Пусто',name_urok[2],name_urok[5],'Пусто','Пусто'],
           [name_urok[1],name_urok[0],'Пусто','Пусто','Пусто'],
           ['Пусто',name_urok[10],name_urok[7],name_urok[13],'Пусто'],
           [name_urok[6],name_urok[3],name_urok[15],name_urok[4],'Пусто'],
           ['Пусто','Пусто',name_urok[8],'Пусто','Пусто'],
           [name_urok[12],name_urok[11],name_urok[9]],'Пусто','Пусто']

Time_Urok =["08:30","10:15","12:00","14:15","16:00"]

def out(num,week):
    i = 0
    s = 'В этот день пар нет'
    if week and len(up_week[num])>0:
        s = ''
        while i < len(up_week[num]):
            if up_week[num][i]!='Пусто':
                s = s +'\n'+ (str(i+1) + '. '+ Time_Urok[i]+' '+ up_week[num][i])+ ' (ауд.'+aud_up_week[num][i]+ ')'
            i = i + 1
    else:
        if (not week) and len(low_week[num])>0:
            s = ''
            while i < len(low_week[num]):
                if low_week[num][i] != 'Пусто':
                    s = s +'\n'+ (str(i+1) + '. '+ Time_Urok[i]+' '+ low_week[num][i])+ ' (ауд.'+aud_low_week[num][i]+ ')'
                i = i + 1
    return s

def Pari_per_Day():
 return

def UPweek_Show(day):
    if day == 'monday':
        return  out(0, True)
    if day == 'tuesday':
        return  out(1, True)
    if day == 'wednesday':
        return  out(2, True)
    if day == 'thursday':
        return  out(3, True)
    if day == 'friday':
        return  out(4, True)
    if day == 'saturday':
        return  out(5, True)
    if day == 'sunday':
        return 'Пар сегодня нет'

def LOWweek_Show(day):
    if day == 'monday':
        return out(0, False)
    if day == 'tuesday':
        return out(1, False)
    if day == 'wednesday':
        return out(2, False)
    if day == 'thursday':
        return out(3, False)
    if day == 'friday':
        return out(4, False)
    if day == 'saturday':
        return out(5, False)
    if day == 'sunday':
        return 'Пар сегодня нет'

#def pos(week,day,num):


def out_now_UP(num,week):
    d = datetime.datetime.now().strftime('%H:%M')
    s =''

    if d<'08:30' and up_week[num][0] != 'Пусто':

            s = s + '\n'  + 'Следующая пара в ' + Time_Urok[0]+', ' + up_week[num][0] + ' ауд.'+aud_up_week[num][0]

    else:
        if d > '08:30' and  d < '10:05' and up_week[num][0] != 'Пусто':
            o = datetime.datetime.now()-datetime.timedelta(hours=8)-datetime.timedelta(minutes=30)
            s = s + '\n' + 'Ты опаздываетешь на 1 пару: ' +up_week[num][0]+ ' ауд.'+aud_up_week[num][0] + ' на ' + str(o.strftime('%H:%M'))
        else:
            if d >= '10:05' and  d <= '10:15' and up_week[num][1] != 'Пусто':
                s = s + '\n' + 'Следующая пара в ' + Time_Urok[1] + ', ' + up_week[num][1] + ' ауд.'+aud_up_week[num][1]
            else:
                if d > '10:15' and d < '11:50' and up_week[num][1] != 'Пусто':
                    o = datetime.datetime.now() - datetime.timedelta(hours=10) - datetime.timedelta(minutes=15)
                    s = s + '\n' + 'Ты опаздываетешь на 2 пару: ' + up_week[num][1] + ' ауд.'+aud_up_week[num][1]+ ' на ' + str(o.strftime('%H:%M'))
                else:

                    if d >= '11:50' and d <= '12:00'and up_week[num][2] != 'Пусто':
                        s = s + '\n' + 'Следующая пара в ' + Time_Urok[2] + ', ' + up_week[num][2]+ ' ауд.'+aud_up_week[num][2]
                    else:
                        if d > '12:00' and d < '13:35'and up_week[num][2] != 'Пусто':
                            o = datetime.datetime.now() - datetime.timedelta(hours=12) - datetime.timedelta(minutes=00)
                            s = s + '\n' + 'Ты опаздываетешь на 3 пару: ' + up_week[num][2]+ ' ауд.'+aud_up_week[num][2] + ' на ' + str(
                                o.strftime('%H:%M'))
                        else:

                            if d >= '13:35' and d <= '14:15'and up_week[num][3] != 'Пусто':
                                s = s + '\n' + 'Следующая пара в ' + Time_Urok[3] + ', ' + up_week[num][3]+ ' ауд.'+aud_up_week[num][3]
                            else:
                                if d > '14:15' and d < '15:50'and up_week[num][3] != 'Пусто':
                                    o = datetime.datetime.now() - datetime.timedelta(hours=14) - datetime.timedelta(
                                        minutes=15)
                                    s = s + '\n' + 'Ты опаздываетешь на 4 пару: ' + up_week[num][3]+ ' ауд.'+aud_up_week[num][3] + ' на ' + str(
                                        o.strftime('%H:%M'))
    if s=='':
        s = 'Следующих пар нет'
    return s

def out_now_LOW(num, week):
    d = datetime.datetime.now().strftime('%H:%M')
    s = ''

    if d < '08:30' and low_week[num][0] != 'Пусто':

        s = s + '\n' + 'Следующая пара в ' + Time_Urok[0] + ', ' + low_week[num][0] + ' ауд.'+aud_low_week[num][0]
    else:
        if d > '08:30' and d < '10:05' and low_week[num][0] != 'Пусто':
            o = datetime.datetime.now() - datetime.timedelta(hours=8) - datetime.timedelta(minutes=30)
            s = s + '\n' + 'Ты опаздываетешь на 1 пару: ' + low_week[num][0]+ ' ауд.'+aud_low_week[num][0] + ' на ' + str(o.strftime('%H:%M'))
        else:

            if d >= '10:05' and d <= '10:15' and low_week[num][1] != 'Пусто':
                s = s + '\n' + 'Следующая пара в ' + Time_Urok[1] + ', ' + low_week[num][1]+ ' ауд.'+aud_low_week[num][1]
            else:
                if d > '10:15' and d < '11:50' and low_week[num][1] != 'Пусто':
                    o = datetime.datetime.now() - datetime.timedelta(hours=10) - datetime.timedelta(minutes=15)
                    s = s + '\n' + 'Ты опаздываетешь на 2 пару: ' + low_week[num][1]+ ' ауд.'+aud_low_week[num][1] + ' на ' + str(
                        o.strftime('%H:%M'))
                else:

                    if d >= '11:50' and d <= '12:00' and low_week[num][2] != 'Пусто':
                        s = s + '\n' + 'Следующая пара в ' + Time_Urok[2] + ', ' + low_week[num][2]+ ' ауд.'+aud_low_week[num][2]
                    else:
                        if d > '12:00' and d < '13:35' and low_week[num][2] != 'Пусто':
                            o = datetime.datetime.now() - datetime.timedelta(hours=12) - datetime.timedelta(
                                minutes=00)
                            s = s + '\n' + 'Ты опаздываетешь на 3 пару: ' + low_week[num][2]+ ' ауд.'+aud_low_week[num][2] + ' на ' + str(
                                o.strftime('%H:%M'))
                        else:

                            if d >= '13:35' and d <= '14:15' and low_week[num][3] != 'Пусто':
                                s = s + '\n' + 'Следующая пара в ' + Time_Urok[3] + ', ' + low_week[num][3]+ ' ауд.'+aud_low_week[num][3]
                            else:
                                if d > '14:15' and d < '15:50' and low_week[num][3] != 'Пусто':
                                    o = datetime.datetime.now() - datetime.timedelta(hours=14) - datetime.timedelta(
                                        minutes=15)
                                    s = s + '\n' + 'Ты опаздываетешь на 4 пару: ' + low_week[num][3]+ ' ауд.'+aud_low_week[num][3] + ' на ' + str(
                                        o.strftime('%H:%M'))



    if s=='':
        s = 'Следующих пар нет'
    return s

def UPweek_Show_now(day):
    if day == 'monday':
        return out_now_UP(0, True)
    if day == 'tuesday':
        return out_now_UP(1, True)
    if day == 'wednesday':
        return out_now_UP(2, True)
    if day == 'thursday':
        return out_now_UP(3, True)
    if day == 'friday':
        return out_now_UP(4, True)
    if day == 'saturday':
        return out_now_UP(5, True)
    if day == 'sunday':
        return 'Пар сегодня нет'

def LOWweek_Show_now(day):
    if day == 'monday':
        return out_now_LOW(0, False)
    if day == 'tuesday':
        return out_now_LOW(1, False)
    if day == 'wednesday':
        return out_now_LOW(2, False)
    if day == 'thursday':
        return out_now_LOW(3, False)
    if day == 'friday':
        return out_now_LOW(4, False)
    if day == 'saturday':
        return out_now_LOW(5, False)
    if day == 'sunday':
        return 'Пар сегодня нет'
#def Uroki(day):
#    if day == 'Saturday':print();

#def naw_uroki():
#    LOWweek_Show(datetime.datetime.now().strftime('%A'));
"""
def show_now_urok(day):
    if day == 'Monday':
        return out(0, False)
    if day == 'Tuesday':
        return out(1, False)
    if day == 'Wednesday':
        return out(2, False)
    if day == 'Thursday':
        return out(3, False)
    if day == 'Friday':
        return out(4, False)
    if day == 'Saturday':
        return out(5, False)
"""

def Kakoy_den():
    return str(translate_day[datetime.datetime.now().strftime('%A').lower()])

def Day_next():
    d = (datetime.datetime.now() + datetime.timedelta(days=1))
    s = 'Завтра '+str(translate_day[d.strftime('%A').lower()])
    s = s + ', ' + Week_name(d)+'\n'
    st = str(UPweek_Show(d.strftime('%A').lower()))
    if st == '':
        st = 'Пар в этот день нет'
    s = s + st
    return s

def Gde_para(d):
    if Week_name(d) == 'Нижняя неделя':
        return str(LOWweek_Show_now(d.strftime('%A').lower()))
    else:
        return str(UPweek_Show_now(d.strftime('%A').lower()))

def para_per_day(week,day):

    if week =='нижняя':
        s = LOWweek_Show(day.lower())
    else:
        s = UPweek_Show(day.lower())
    return s

if 'ff' in 'f':
    print('ffqw')
#print(para_per_day('верхняянеделя','monday'))
"""
print(UPweek_Show_now('Monday'));
print(UPweek_Show_now('Tuesday'));
print(UPweek_Show_now('Wednesday'));
print(UPweek_Show_now('Thursday'));
print(UPweek_Show_now('Friday'));
print(UPweek_Show_now('Saturday'));

print(datetime.datetime.now().strftime('%H:%M'))
print(datetime.datetime.now().strftime('%A'))
print(Week_name())
print(LOWweek_Show('Monday'))



print(Week());
day_name=datetime.datetime.now().strftime('%A');
print(day_name);
if Week() == 'Нижняя неделя':
    if day_name == 'Saturday':print();
"""