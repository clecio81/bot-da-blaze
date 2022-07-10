import csv
import json
import requests
import telebot
from time import sleep
from datetime import datetime
from notifypy import Notify
from pushbullet import Pushbullet


def count(time, win:int, loss:int):
    with open('count.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([f'{time}', win, f'{loss}\n'])  


# desktop notification settings
def desktop_notification(message):
    notification = Notify()
    notification.title = 'Blaze'
    notification.message = message
    notification.icon = r'C:\Users\User\Downloads\python projects\blaze_bot\blaze-icon.png'
    notification.send()

# phone notifications
# API_KEY = 'o.9mKgLukDRUkGzzaWN9DIC0aqy3ixNHKj'
# pb = Pushbullet(API_KEY)

def request():
    req = requests.get('https://blaze.com/api/roulette_games/recent')
    output = json.loads(req.text)
    list_past_results = [{'cor': row['color'], 'numero': row['roll']} for row in output[:4]]
    return list_past_results


def main_request():
    while True:
        
        list_past_results = request()
        if list_past_results[0]['cor'] == list_past_results[1]['cor'] and list_past_results[1]['cor'] == list_past_results[2]['cor'] and list_past_results[2]['cor'] == list_past_results[3]['cor']:
            #push = pb.push_note('Blaze', 'Apostar')

            return apostar(list_past_results)

        print('request feito:', datetime.now())
        sleep(10)


def apostar(lista):
    if lista[0]['cor'] == 2:
        desktop_notification('Apostar no vermelho e no branco')
        # bot_msg('Apostar no vermelho e no branco.')
    if lista[0]['cor'] == 1:
        desktop_notification('Apostar no preto e no branco')       
        # bot_msg('', 'Apostar no preto e no branco.')
    sleep(28)
    checagem()


def checagem():
    
    win = 0
    loss = 0
    
    list = request()
    if list[0]['cor'] != list[1]['cor']:
        desktop_notification('WIIINNNN')
        win += 1
        print('WIINN')
    else:
        desktop_notification('Vamos para a primeira gale. \nDobre a aposta e repita a cor')
        print('Primeira gale')
        sleep(28)
    
        list = request()
        if list[0]['cor'] != list[1]['cor']:
            desktop_notification('WIIINNNN')
            win += 1
            print('WINN')
        else:
            desktop_notification('Vamos para a segunda gale. \nDobre a aposta e repita a cor.')
            print('Segunda gale')
            sleep(28)
    
            list = request()
            if list[0]['cor'] != list[1]['cor']:
                desktop_notification('WIIINNNN')
                win += 1
                print('WINN')
            else:
                desktop_notification('Loss')
                loss += 1
                print('loss')

    time = datetime.now()
    count(time, win, loss)
    
    sleep(38)
    main_request()

main_request()

# Cor 2 = Preto | Cor 1 = Vermelho | Cor 0 - Branco