from logging import exception
from sqlite3.dbapi2 import Cursor
from time import time
import telebot
import sqlite3
from telebot import types
bot=telebot.TeleBot("2010879791:AAH3c7s9NYQmltGCFSs6XEzSoU6f0Nz-mzg")

conn = sqlite3.connect("database_bmk.db")
cursor = conn.cursor()
cursor.execute("SELECT name, linktosite, linktopng, sostav, grypa FROM 'kolbasi'")

DataBMK = []
for result in cursor:
    DataBMK.append(result)
cursor.close()

# обработчик команд -------------------------------------------------------------------
# создаем кнопки при старте и регистрируем пользователя*********************************************
@bot.message_handler(commands=['start','рег','users'])
def send_echo(message): 
    textif=message.text[0 : 4]
    if message.text=='/start':
        bot.send_message(message.chat.id, 'Привествую! напиши название продукции')
        bot.send_message(message.chat.id, 'Для регистрации введите /рег Фамилия Имя отчество')
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Колбасы','Заморозка','О нас')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard)
        bot.send_message( 909421591 , 'Подключился новый клиент: '+ str(message.chat.id))

    elif message.text=='/users':
        cursor = sqlite3.connect("database_bmk.db").cursor()
        cursor.execute( "SELECT * FROM Users")
        for result in cursor:
            bot.send_message( 909421591 , str(result[1]) +' '+ str(result[2]))
        cursor.close()

    elif textif=='/рег':
        textif = message.text[ 5: len(message.text) ]
        cursor = sqlite3.connect("database_bmk.db").cursor()
        zapros = str("INSERT INTO 'Users' (id_telegram, name) VALUES ( " + str(message.chat.id) + ",'" + textif + "')")
        bot.send_message( 909421591 , 'Зарегестрировался: '+ textif)
        try:
            cursor.execute( zapros)
        except:
            bot.send_message(message.chat.id, 'Вы уже зарегестрированны!!!')
        conn.commit()
        cursor.close()
# выводим пользователю список колбас в кнопки из выбраной категории ******************************
def List_button(message, data):
        if data == 'Вареные': data = 'Колбасы варёные'
        elif data == 'Ветчины': data = 'Ветчины варёные в оболочке'
        elif data == 'Ливерные': data = 'Колбасы ливерные, кровяные, паштет'
        elif data == 'Полукопы': data = 'Колбасы полукопчёные'
        elif data == 'Сырокопы': data = 'Колбасы сырокопчёные'
        elif data == 'Сыровяленые': data = 'Колбасы сыровяленые'
        elif data == 'Варенокопченые': data = 'Колбасы варёнокопчёные'
        elif data == 'Сосиски': data = 'Сосиски'
        elif data == 'Сардельки': data = 'Сардельки'
               
        inline_kb1 = telebot.types.InlineKeyboardMarkup()
        cursor=sqlite3.connect("database_bmk.db").cursor()
        cursor.execute("SELECT name FROM 'kolbasi' WHERE grypa = '" + str(data) + "'")
        for result in cursor:
            inline_btn_1 = telebot.types.InlineKeyboardButton(result[0], callback_data=result[0])
            inline_kb1.add(inline_btn_1)
        bot.send_message(message.chat.id,'Выберите позицию', reply_markup=inline_kb1)
        bot.send_message(909421591, 'user=' + str(message.chat.id) + ' запросил ' + data)
        cursor.close()
# кнопка меню О НАС  *****************************************************************************
def O_nas(message):
    bot.send_message(message.chat.id, 'ОСНОВАН В 1944Г.')
    str_temp = str('«Бендерский мясокомбинат» признанный лидер среди предприятий пищевой промышленности Приднестровья по производству мясных продуктов. Производственные мощности ЗАО «Бендерский мясокомбинат» на сегодняшний день составляют:- по выработке мяса скота – 45 тн в смену;- по выработке колбасных изделий – 20 тн в смену;- по выпуску полуфабрикатов – 10 тн в смену;  - по выпуску консервов – 15000 ф.б. в смену.')
    bot.send_message(message.chat.id, str_temp)
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=4uqlL4FFQAI&t=116s')
# кнопка меню В НАЧАЛО  ************************************************************************** 
def vnachalo(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Колбасы','Заморозка','О нас')
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard)
# Выводим список колбас и делаем меню кнопок******************************************************
def kolbasi(message):
    #i=0
    #strint_otvet = ''

    #while i < len(DataBMK):
    #    strint_otvet = strint_otvet + DataBMK[i][0] + ' \n '
    #    i = i + 1
    #bot.send_message(message.chat.id, strint_otvet,  parse_mode='HTML', disable_web_page_preview=True)
                
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Вареные', 'Ветчины','Ливерные')
    keyboard.row('Полукопы', 'Сырокопы','Сыровяленые')
    keyboard.row('Варенокопченые', 'Сосиски','Сардельки')
    keyboard.row('В начало')
    bot.send_message(message.chat.id, 'Введите название или выберите категорию ', reply_markup=keyboard)

# обработка кнопок в сообщениях
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
        i=0
        while i < len(DataBMK) and call.data.upper() != DataBMK[i][0].upper():
                i = i + 1       
        if i < len(DataBMK):
                     bot.send_photo(call.message.chat.id, DataBMK[i][2]) 
                     bot.send_message(call.message.chat.id, DataBMK[i][0] + '\n' + DataBMK[i][3]) 
                     bot.send_message(909421591, 'user=' + str(call.message.chat.id) + ' запросил ' + DataBMK[i][0]) 
        
        conn = sqlite3.connect("database_bmk.db")
        cursor = conn.cursor()
        zapros = str("INSERT INTO 'Statistika' (id_telegram, grypa) VALUES ( " + str(call.message.chat.id) + ",'" + str(DataBMK[i][0]) + "')")
        cursor.execute( zapros)
        conn.commit()

        bot.answer_callback_query(call.id)

# обработчик текстовых сообщений ------------------------------------------------------
@bot.message_handler(content_types=['text'])
def send_echo(message):
        
        # Ищем позицию в базе
        if   message.text == 'Вареные':         List_button(message, message.text)
        elif message.text == 'Ветчины':         List_button(message, message.text)
        elif message.text == 'Ливерные':        List_button(message, message.text)
        elif message.text == 'Полукопы':        List_button(message, message.text)
        elif message.text == 'Сырокопы':        List_button(message, message.text)
        elif message.text == 'Сыровяленые':     List_button(message, message.text)
        elif message.text == 'Варенокопченые':  List_button(message, message.text)
        elif message.text == 'Сосиски':         List_button(message, message.text)
        elif message.text == 'Сардельки':       List_button(message, message.text)
        
        elif message.text == 'В начало':  vnachalo(message)
        elif message.text == 'О нас':     O_nas(message)
        elif message.text == 'Колбасы':   kolbasi(message)
        elif message.text == 'Заморозка': bot.send_message(message.chat.id, 'в разработке')
        elif message.text == 'Автор':     bot.send_message(message.chat.id, 'Дорош Анатолий Петрович')
       
        i=0
        while i < len(DataBMK) and message.text.upper() != DataBMK[i][0]:
                i = i + 1

        if i < len(DataBMK):
                bot.send_photo(message.chat.id, DataBMK[i][2]) 
                bot.send_message(message.chat.id, DataBMK[i][3])
                bot.send_message(909421591, 'user=' + str(message.chat.id) + ' запросил ' + DataBMK[i][0])

if __name__=='__main__':
        while True:
                try:
                        bot.infinity_polling(timeout=30, long_polling_timeout = 5)   
                except Exception as e:
                        time.sleep(3) 
                        print(e)