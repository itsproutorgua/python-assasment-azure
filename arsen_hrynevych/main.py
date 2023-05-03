import telebot
from flask import Flask, request, Response
from api import API

bot = telebot.TeleBot(API)

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return Response('ok', status=200)
    

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "HI")


@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, "Please continue")


if __name__ == '__main__':
    app.run()
