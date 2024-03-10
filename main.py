import telebot
from telebot import types
from config import TOKEN, photo_url1, TO_CHAT_ID
from question import quiz, question1, callback_query2, point
from reviews import reviews, callback_query3, rating

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id,
                   photo=photo_url1,
                   caption=f'Приветствую {message.from_user.first_name}! Я могу сделать викторину для тебя и '
                           f'определить какое у тебя тотемное жтвотное, мои вопросы простые, это займет '
                           f'у тебя около минуты')
    menu(message)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    btn4 = types.KeyboardButton('Оценить бота')
    btn6 = types.KeyboardButton('Узнать оценки бота')
    btn5 = types.KeyboardButton('⚠Связаться с работником⚠')

    markup.add(btn8, btn4, btn5, btn6)
    bot.send_message(message.chat.id, "Я работаю только от кнопок, которые у тебя находятся внизу, либо же на экране "
                                      "в моих сообщениях. Если возникли какие-то сложности, вы можете попросить помощи "
                                      "у сторудника, нажав кнопку СВЯЗАТЬСЯ С СОТРУДНИКОМ. \nТак же вы можете поставить "
                                      "оценку боту, это поспособствует усовершенствованию ", reply_markup=markup)


@bot.message_handler(commands=['svyaz'])
def svyz(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn8 = types.KeyboardButton("Главное меню")
    markup.add(btn8)
    bot.send_message(message.chat.id, "В ближайшее время с вами свяжется сотрудник", reply_markup=markup)
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


@bot.message_handler(commands=['Main_menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Помощь')
    btn2 = types.KeyboardButton('Животные')
    btn3 = types.KeyboardButton('Викторина')

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "❓Помощь❓ /  🐺Животные🐨 / "
                                           "🎁Викторина🎁", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    callback_query2(call)
    callback_query3(call)


def animals1(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button9 = types.InlineKeyboardButton(text="Перейти на сайт", url="moscowzoo.ru")
    url_button10 = types.InlineKeyboardButton(text="Перейти в группу в телеграмме",
                                              url="https://t.me/Moscowzoo_official")
    keyboard.add(url_button9, url_button10)
    bot.send_message(message.chat.id, "Данный бот был разработан для дополнительного контента, но "
                                      "вы можете перейти в телеграм канал и сайт, где есть вся "
                                      "информация о животных", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Главное меню":
        bot.send_message(message.chat.id, text="Вы вернулись в Главное меню")
        menu(message)
    elif message.text == "Помощь":
        help(message)
    elif message.text == "Викторина":
        quiz(message)
    elif message.text == "Оценить бота":
        reviews(message)
    elif message.text == "Начать викторину":
        question1(message)
    elif message.text == "⚠Связаться с работником⚠":
        svyz(message)
    elif message.text == "Узнать оценки бота":
        rating(message)
    elif message.text == "Животные":
        animals1(message)
    else:
        bot.send_message(message.chat.id, text="Ничего не надо писать, нажимай на кнопки :)", )


print(point)

bot.polling(none_stop=True)
