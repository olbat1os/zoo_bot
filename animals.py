import telebot
from config import TOKEN
from telebot import types
from config import photo_url2, photo_url3, photo_url4, photo_url5, photo_url6, photo_url7, photo_url8

bot = telebot.TeleBot(TOKEN)
text11 = 'этот бот дал мне тест и я выяснил, что мое тотемное животное '
text12 = " твоим тотемным животным является"
text13 = 'В Московском зоопарке существует система ОПЕКИ, вы можете запросто стать опекуном своего тотемного животного,' \
         ' для подробной информации вы можете спросить у сотрудника нажав --> /svyaz '


def volk(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + '🐺')
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url2,
                   caption=f'{call.message.chat.username}{text12} волк!  '
                           f'\nВолк — символ свободы и силы. Это тотемное животное наделяет своего обладателя '
                           f'твердым характером, сильной интуицией и чувствительностью. Несмотря на то, что в '
                           f'природе волки живут стаями, данный тотем также ассоциируется с любовью к уединению и '
                           f'недоверчивостью. \n{text13}', reply_markup=markup)


def lev(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🦁")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url3,
                   caption=f'{call.message.chat.username}{text12} лев'
                           f'\nЛев — достаточно противоречивая тотемная фигура. Несмотря на большое количество '
                           f'положительных качеств — храбрость, силу, способность вести за собой, благородство, '
                           f'отзывчивость, присутствуют и отрицательные черты, самой заметной из которых выступает '
                           f'эгоистичность. Проблемы других членов общества редко волнуют обладателей этого тотема, '
                           f'потому что лев должен быть в центре, и мир должен кружиться вокруг него. Но не все так '
                           f'плохо😁, в экстремальной ситуации помощь такого человека будет незаменима. Он способен'
                           f' переключить фокус внимания ради важного человека.\n{text13}', reply_markup=markup)


def lisa(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🦊")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url4,
                   caption=f'{call.message.chat.username}{text12} лиса'
                           f'\nЧеловек с таким тотемом —Хозяйственный, запасливый, артистичный и '
                           f'целеустремленный это все выраженно в людях-лисах. Они смогут найти выгоду и реализоваться '
                           f'в любых условиях.! Найдут выход из самых патовых ситуаций, всегда выходя победителем. '
                           f'Очень мобильны и приспосабливаемы.\n{text13}', reply_markup=markup)


def tiger(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🐯")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url5,
                   caption=f'{call.message.chat.username}{text12} тигр! '
                           f'\nТигр — это творец и разрушитель одновременно. Ему также свойственно королевское '
                           f'достоинство, жестокость, сила, власть, мужество и ярость, которая нужна ему как '
                           f'защитнику. Тигр считается одним из сильнейших тотемов, и не каждый человек способен '
                           f'выдержать его напор. Если тигр выбрал вас, будьте готовы стать королём в своём '
                           f'собственном замке. Отныне Вы Правитель своей жизни.\n{text13}', reply_markup=markup)


def olen(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🫎")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url6,
                   caption=f'{call.message.chat.username}{text12} олень!  '
                           f'\nОлень — благородное коллективное животное, которое наделяет своего обладателя '
                           f'легким и приятным нравом. Людям этого тотема не составляет труда быстро стать своим в '
                           f'новой компании. Внешне Олень выглядит хрупким и нежным, но на самом деле он очень '
                           f'выносливый и быстро восстанавливается даже после самых неприятных '
                           f'ударов судьбы.\n{text13}', reply_markup=markup)


def medved(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🐻")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url7,
                   caption=f'{call.message.chat.username}{text12} медведь!  '
                           f'\nЭто тотемное животное помогает своим обладателям найти гармонию в жизни, учит '
                           f'наслаждать моментом и ценить то, что есть. Медведи в первую очередь, конечно, '
                           f'ассоциируются с силой и дальновидностью. В природе эти животные царствуют в лесу и '
                           f'ревностно охраняют свою территорию. Они всегда готовы сражаться, но при этом в очень '
                           f'редких случаях нападают первыми. \n{text13}', reply_markup=markup)


def loshad(call):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Поделиться",
                                             switch_inline_query=text11 + "🐴")
    markup.add(info_button)
    bot.send_photo(call.message.chat.id,
                   photo=photo_url8,
                   caption=f'{call.message.chat.username}{text12} лошадь!  '
                           f'\nЧеловек с таким тотемом — смелый, честный, верный и преданный, постоянно находится'
                           f' в движении. Ему просто необходимо отсутствие ограничений, иначе он теряет интерес к '
                           f'жизни. Тотем Лошади может помочь в любых делах, наполнить энергией, активировать '
                           f'творческий поток и вдохновение.\n{text13}', reply_markup=markup)
