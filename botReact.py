#чтобы работало, создаем сессию и аторизируемся на сайте: https://my.telegram.org/apps
from pyrogram import Client, filters  # Импорт filters
from loguru import logger

call = [] # id человека, на чьи сообщения реагируем, если надо
app = Client('my_account')
group = [] # id чата в котором будем реагировать, если их несколько, то через запятую

@app.on_message(filters.text)  # Фильтр для текстовых сообщений
def main(_, message):
    try:
        if message.chat.id in group:
            logger.info(f"FIND NEW MESSAGE - {message.chat.id} | {message.from_user.id}") # покажет id-ники
            if message.from_user.id in call:
                logger.info(f"User {message.from_user.id} found in call list, sending emoji")
                app.send_reaction(message_id=message.id, chat_id=message.chat.id, emoji="🤡")
            else:
                logger.error(f"User {message.from_user.id} is not in the call list")
        else:
            logger.error(f"Message not in target group | {message.chat.id}")
    except Exception as e:
        logger.error(f"Error while processing message: {e}")

app.run()

