import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from secrets import API_TOKEN
from note import *

updater = Updater(token=API_TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет, пупсик, я бот Альберта, задавай свои грязные вопросики")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def create_note_handler(update, context):
    try:
        # Получить текст заметки из сообщения пользователя
        note_text = update.message.text
        # Получить название заметки из сообщения пользователя
        note_name = update.message.chat_id
        # Создать заметку с помощью функции create_note(note_text, note_name)
        create_note("22", "1")
        # Отправить пользователю подтверждение, что заметка создана
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

# Добавить функцию create_note_handler как CommandHandler для команды /create
updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))



updater.start_polling()