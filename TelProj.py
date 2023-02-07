import telebot
from telebot import types
token='6084814748:AAF7qWZmEKFMv2LcH1noGMcPjVhwrVX1pnE'
bot=telebot.TeleBot(token)
import requests

url = "https://hotels4.p.rapidapi.com/v2/get-meta-data"

headers = {
	"X-RapidAPI-Key": "47e8d0590amshf46996fbb6dbbd1p16c668jsnead9e66427e6",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Здраствуй " + message.from_user.first_name + " "  + message.from_user.last_name);
        select_option(message)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start');

def select_option(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура 
    help = types.InlineKeyboardButton(text='help', callback_data='help'); #кнопка «Да»
    keyboard.add(help); #добавляем кнопку в клавиатуру
    lowprice= types.InlineKeyboardButton(text='lowprice', callback_data='lowprice');
    keyboard.add(lowprice);
    highprice= types.InlineKeyboardButton(text='highprice', callback_data='highprice');
    keyboard.add(highprice);
    highprice= types.InlineKeyboardButton(text='bestdeal', callback_data='bestdeal');
    keyboard.add(highprice);
    history= types.InlineKeyboardButton(text='history', callback_data='history');
    keyboard.add(history);
    question = "Выбирете опцию"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
   

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "help":
        bot.send_message(call.message.chat.id, 'help : )');
    elif call.data == "lowprice":
        bot.send_message(call.message.chat.id, 'help : )');
    elif call.data == "highprice":
        bot.send_message(call.message.chat.id, 'highprice : )');
    elif call.data == "bestdeal":
        bot.send_message(call.message.chat.id, 'bestdeal : )');
    elif call.data == "history":
        bot.send_message(call.message.chat.id, 'history : )');
bot.polling(none_stop=True, interval=0)