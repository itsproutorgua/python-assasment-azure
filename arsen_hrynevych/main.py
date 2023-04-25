import logging
from api import API
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


@app.route('/webhooks', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = request.get_json()
        application.process_update(update)
    return 'ok'


if __name__ == '__main__':
    application = ApplicationBuilder().token(API).build()

    application.add_handler(CommandHandler('start', lambda update, context: context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me")))

    application.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), lambda update, context: context.bot.send_message(
            chat_id=update.effective_chat.id, text=update.message.text)))

    application.add_handler(MessageHandler(filters.COMMAND, lambda update, context: context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")))
    
    WEBHOOK_URL = "https://9879509a-4f0e-4afe-88fe-f98cf5b44996.webhook.we.azure-automation.net/webhooks?token=3tA7lGLWnep7VceAKFXaGyqWrGZ9DQILJ5od8MtNoCE%3d"
    application.set_webhook(WEBHOOK_URL)
    app.run()

