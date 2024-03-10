import telebot
from config import TOKEN
from telebot import types
from animals import lev, volk, tiger, lisa, loshad, medved, olen

bot = telebot.TeleBot(TOKEN)

point = 0
lvl = 0


@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.send_message(message.chat.id, text="Эта викторина определит какое у тебя тотемное животное🎁", )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Главное меню')
    btn2 = types.KeyboardButton('Начать викторину')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "❗Главное меню❗ /  "
                                           "🎁Начать викторину🎁", reply_markup=markup)


def question1(message):
    global point
    global lvl
    point = 0
    lvl = 0
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Работяга", callback_data='1')
    info_button2 = types.InlineKeyboardButton("Оптимист", callback_data='2')
    info_button3 = types.InlineKeyboardButton("Лидер", callback_data='3')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Кто ты в этой жизни", reply_markup=markup)
    question2(message)


def question2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Заработать много денег", callback_data='4')
    info_button2 = types.InlineKeyboardButton("Познать себя и мир вокруг", callback_data='5')
    info_button3 = types.InlineKeyboardButton("Крепкую и дружную семью", callback_data='6')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Что вы хотите от этой жизни", reply_markup=markup)
    question3(message)


def question3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    info_button1 = types.InlineKeyboardButton("Одиночества", callback_data='7')
    info_button2 = types.InlineKeyboardButton("Любви", callback_data='8')
    info_button3 = types.InlineKeyboardButton("Предательства", callback_data='9')
    markup.add(info_button1, info_button2, info_button3)
    bot.send_message(message.chat.id, "Что вы больше всего боитесь?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query2(call):
    global point
    global lvl
    if call.data == "1":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "2":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "3":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="1ый вопрос \U00002705", reply_markup=None)
    if call.data == "4":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "5":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "6":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="2ой вопрос \U00002705", reply_markup=None)
    if call.data == "7":
        point += 1
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if call.data == "8":
        point += 2
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if call.data == "9":
        point += 3
        lvl += 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3ий вопрос \U00002705", reply_markup=None)
    if lvl == 3:
        bot.send_message(call.message.chat.id, " Викторина заверешена!")
        if point == 3:
            olen(call)
        if point == 4:
            lisa(call)
        if point == 5:
            loshad(call)
        if point == 6:
            tiger(call)
        if point == 7:
            medved(call)
        if point == 8:
            volk(call)
        if point == 9:
            lev(call)

    print(point)
