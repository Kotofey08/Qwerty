import telebot
from telebot import types
token = '6947899996:AAFkySXMwxz4HtCEyYG8VP1oTTRukmoIl6Q'
bot = telebot.TeleBot(token)
'Команды '
@bot.message_handler(commands=['start'])    # строка, которая позволяет принимать команду "старт" от пользователя.
def start_message(message):
    mess= f'Привет,<b>{message.from_user.first_name}</b> <u> </u> '
    bot.send_message(message.chat.id,mess, parse_mode='html')   # send_message отправляет данные пользователю
    '''''
@bot.message_handler(content_types=['document'])
def get_user_doc (message):
    bot.send_message(message.chat.id, 'Ваш документ принят')
    'Создание кнопок'
'''''

@bot.message_handler(commands=['help'])
def info(message):
    markup = types.ReplyKeyboardMarkup()
    start = types.InlineKeyboardButton('/start')
    bot.send_message(message.chat.id, 'Лови.', reply_markup=markup)
    guide = types.InlineKeyboardButton('Гайд',url = 'https://www.youtube.com/watch?v=xvFZjo5PgG0&t=3s')
    Rick = types.InlineKeyboardButton('Рикролл',url = '')
    markup.add(guide, start)
sticker_ids = ['CAACAglAAxkBAAEB7ujlUOk1aR-mQCgLgvcMLVmXUvIJnlAACoA-ADlp-MDmce7YYzVgABVTME']
@bot.message_handler(content_types='sticker')
def handle_sticker(message):
    random_sticker_id = random.choice(sticker_ids)
    bot.send_sticker(message.chat.id,random_sticker_id)


'Основной цикл программы'
bot.polling(none_stop=True)  # () Ожидает новый сообщений пока не остановим вручную.
# none_stop=True - перезапускается в случае ошибки
# (interval=<seconds>) - Обновляет информацию каждые seconds секунд.
'''''
@bot.message_handler(commands=['help'])  # выполнение команды "help"
def info(message):
    markup = types.ReplyKeyboardMarkup()  # создание объекта кнопки. ReplyKeyboardMarkup - кнопки внизу панели
    # InlineKeyboardMarkup - кнопки в текстовом сообщении
    #('Гайд.', url='https://www.youtube.com/watch?v=xvFZjo5PgG0&t=3s')
    start = types.InlineKeyboardButton('/start')  # Создание кнопки, по нажатию которой отправляет "/start"
    #markup.add(start, inf)  # добавляем все кнопки в переменную markup
    bot.send_message(message.chat.id, 'Команды для бота', reply_markup=markup)    # отправляем пользователю кнопк@bot.message_handler(content_types=['photo'])
#sticker_ids = ['CAACAglAAxkBAAEB7ujlUOk1aR-mQCgLgvcMLVmXUvIJnlAACoA-ADlp-MDmce7YYzVgABVTME']
'''''