import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, MessageHandler, filters

logging.basicConfig(level=logging.WARNING, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    filename="bot.log",
                    filemode="a")

load_dotenv()

TOKEN = os.getenv('GREETER_TOKEN')

async def greet_user(update: Update, context: CallbackContext):
        user = update.message.new_chat_members[0]
        user_display_name = f"{user.first_name}"
        if user.username is not None:
            mention = f"@{user.username}"
            user_display_name = f"{user.first_name} {mention}"

        await update.message.reply_html(f"Привет, {user_display_name} ! Это чат-флудилка. Здесь мы разговариваем на «ты», обсуждаем котиков, гусей, еду и даже иногда работу. И у нас есть несколько правил:\n1. Зайдя в чат не молчи, вливайся в любую дискуссию или запускай свою.\n2. За политику и переход на личности — бан на сутки.\n3. Избыточный кринж и мат не приветствуются.\n\nПлата за вход — фото домашнего животного (кактусы тоже считаются).")


def main():
    print("I'm working")

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, greet_user))

    application.run_polling()

if __name__ == '__main__':
    main()