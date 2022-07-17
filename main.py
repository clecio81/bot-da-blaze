import telebot
from functions import main_request, results

# Creating bot 
TOKEN = '5429855911:AAHKI_y_L2dy7pyyapj2dM0oB6eNeSHwPIU'
bot = telebot.TeleBot(TOKEN, parse_mode=None)



@bot.message_handler(commands=['resultado'])
def send_stats(message):
    a = results()
    string = f'''Wins: {a['wins']} \nErros: {a['losses']} \nPrimeira tentativa: {a['prim_tent']} \nPrimeira gale: {a['prim_gale']} \nSegunda gale: {a['seg_gale']} \nWinrate: {a['porcentagem']}'''
    bot.reply_to(message, text=string)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message('-1001772338760', '\U0001f4c8 \U0001f4c8 LIGANDO O ROBOZINHO DO PIX \U0001f4c8 \U0001f4c8')
    main_request(bot)

bot.infinity_polling()
