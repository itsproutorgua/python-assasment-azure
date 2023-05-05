import telegram
from flask import Flask, request

app = Flask(__name__)

bot = telegram.Bot(token="5801516775:AAH9wFneIOuk6boY1u4hZxht6IVKcpFgRSA")

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        text = update.message.text
        chat_id = update.message.chat_id
        bot.sendMessage(chat_id=chat_id, text="Hello! You said: {}".format(text))
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
