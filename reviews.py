import telebot
from telebot import types
from config import TOKEN
from animals import text13

bot = telebot.TeleBot(TOKEN)
client = 0
rew = 0


@bot.message_handler(commands=['reviews'])
def reviews(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("1", callback_data='Единица')
    info_button2 = types.InlineKeyboardButton("2", callback_data='Двойка')
    info_button3 = types.InlineKeyboardButton("3", callback_data='Тройка')
    info_button4 = types.InlineKeyboardButton("4", callback_data='Четверка')
    info_button5 = types.InlineKeyboardButton("5", callback_data='Пятерка')

    markup.add(info_button1, info_button2, info_button3, info_button4, info_button5)
    bot.send_message(message.chat.id, "Оценка бота проимходит по пятибальной шкале", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query3(call):
    global client
    global rew
    if call.data == "Единица":
        client += 1
        rew += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!☹️", reply_markup=None)
    if call.data == "Двойка":
        client += 1
        rew += 2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!😟", reply_markup=None)
    if call.data == "Тройка":
        rew += 3
        client += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!😑", reply_markup=None)
    if call.data == "Четверка":
        client += 1
        rew += 4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!🙂", reply_markup=None)
    if call.data == "Пятерка":
        rew += 5
        client += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Спасибо за оценку!🥹", reply_markup=None)


def rating(message):
    global rew
    global client
    if client == 0:
        bot.send_message(message.chat.id, text="Оценок пока нет, станьте первым!", )
    else:
        rat = rew // client
        bot.send_message(message.chat.id, text=f"Количество  поставленных оценок  {client}"
                                               f"\nСредняя оценка бота- {rat}", )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    markup.add(btn8)
    bot.send_message(message.chat.id, f"{text13}", reply_markup=markup)
