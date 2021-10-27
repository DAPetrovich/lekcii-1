from time import time
import telebot
from telebot import types
bot=telebot.TeleBot("2010879791:AAH3c7s9NYQmltGCFSs6XEzSoU6f0Nz-mzg")

DataBMK = []

def Loadfile():
        with open('d:\Учеба\Python\BMK\BMK.csv','r') as filexxx:
             DataFromDoc=filexxx.read()
        i=0

        while i < len(DataFromDoc):
                itemlist = []
                j=0
                while j < 4 :   
                        item1=''
                        while DataFromDoc[i] != ';':
                               item1 = item1 + str(DataFromDoc[i])
                               i = i + 1
                        i = i + 1
                        j = j + 1
                        itemlist.append(item1)
                item1=''
                while DataFromDoc[i] != '\n':
                        item1 = item1 + str(DataFromDoc[i])
                        i = i + 1
                i = i + 1
                itemlist.append(item1)

                DataBMK.append(itemlist)

Loadfile()

# обработчик команд -------------------------------------------------------------------
# создаем кнопки *******************************************************************
@bot.message_handler(commands=['start'])
def send_echo(message):
                
        bot.send_message(message.chat.id, 'Привествую! просто напиши название продукции')
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Колбасы','Заморозка','О нас')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard)

# выводим пользователю список колбас в кнопки из выбраной категории
def List_button(message, data):
        if data == 'Вареные': data = 'Колбасы варёные'
        if data == 'Ветчины': data = 'Ветчины варёные в оболочке'
        if data == 'Ливерные': data = 'Колбасы ливерные, кровяные, паштет'
        if data == 'Полукопы': data = 'Колбасы полукопчёные'
        if data == 'Сырокопы': data = 'Колбасы сырокопчёные'
        if data == 'Сыровяленые': data = 'Колбасы сыровяленые'
        if data == 'Варенокопченые': data = 'Колбасы варёнокопчёные'
        if data == 'Сосиски': data = 'Сосиски'
        if data == 'Сардельки': data = 'Сардельки'
               
        inline_kb1 = telebot.types.InlineKeyboardMarkup()

        i=0
        while i < len(DataBMK):
                if DataBMK[i][4] == data:
                        inline_btn_1 = telebot.types.InlineKeyboardButton(DataBMK[i][0], callback_data=DataBMK[i][0])
                        inline_kb1.add(inline_btn_1)
                i = i + 1

        bot.send_message(message.chat.id,'Выберите позицию', reply_markup=inline_kb1)

# обработка кнопок в сообщениях
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
        
        i=0
        while i < len(DataBMK) and call.data.upper() != DataBMK[i][0].upper():
                i = i + 1  
       
        if i < len(DataBMK):
                     bot.send_photo(call.message.chat.id, DataBMK[i][2]) 
                     bot.send_message(call.message.chat.id, DataBMK[i][0] + '\n' + DataBMK[i][3])  
        
        bot.answer_callback_query(call.id)

# обработчик текстовых сообщений ------------------------------------------------------
@bot.message_handler(content_types=['text'])
def send_echo(message):
        
        # Ищем позицию в базе
        if message.text == 'Вареные':         List_button(message, message.text)
        if message.text == 'Ветчины':         List_button(message, message.text)
        if message.text == 'Ливерные':        List_button(message, message.text)
        if message.text == 'Полукопы':        List_button(message, message.text)
        if message.text == 'Сырокопы':        List_button(message, message.text)
        if message.text == 'Сыровяленые':     List_button(message, message.text)
        if message.text == 'Варенокопченые':  List_button(message, message.text)
        if message.text == 'Сосиски':         List_button(message, message.text)
        if message.text == 'Сардельки':       List_button(message, message.text)
        i=0
        while i < len(DataBMK) and message.text.upper() != DataBMK[i][0]:
                i = i + 1

        if i < len(DataBMK):
                bot.send_photo(message.chat.id, DataBMK[i][2]) 
                bot.send_message(message.chat.id, DataBMK[i][3])
        
        if message.text == 'В начало':
                keyboard = telebot.types.ReplyKeyboardMarkup(True)
                keyboard.row('Колбасы','Заморозка','О нас')
                bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard)  

        if message.text == 'О нас':
               bot.send_message(message.chat.id, 'ОСНОВАН В 1944Г.')
               str_temp = '«Бендерский мясокомбинат» признанный лидер среди предприятий пищевой промышленности Приднестровья по производству мясных продуктов. Производственные мощности ЗАО «Бендерский мясокомбинат» на сегодняшний день составляют:- по выработке мяса скота – 45 тн в смену;- по выработке колбасных изделий – 20 тн в смену;- по выпуску полуфабрикатов – 10 тн в смену;  - по выпуску консервов – 15000 ф.б. в смену.'
               bot.send_message(message.chat.id, str_temp)
               bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=4uqlL4FFQAI&t=116s')

        if message.text == 'Колбасы':
                i=0
                strint_otvet = ''
                while i < len(DataBMK):
                        strint_otvet = strint_otvet + DataBMK[i][0] + ' \n '
                        #strint_otvet = strint_otvet + '<a href="' + DataBMK[i][1] +'">'+ DataBMK[i][0] + '</a>'  + ' \n '
                        i = i + 1
                bot.send_message(message.chat.id, strint_otvet,  parse_mode='HTML', disable_web_page_preview=True)
                
                keyboard = telebot.types.ReplyKeyboardMarkup(True)
                keyboard.row('Вареные', 'Ветчины','Ливерные')
                keyboard.row('Полукопы', 'Сырокопы','Сыровяленые')
                keyboard.row('Варенокопченые', 'Сосиски','Сардельки')
                keyboard.row('В начало')
                bot.send_message(message.chat.id, 'Введите название или выберите категорию ', reply_markup=keyboard)
        if message.text == 'Заморозка':
                bot.send_message(message.chat.id, 'в разработке')
        if message.text == 'Автор':
                bot.send_message(message.chat.id, 'Дорош Анатолий Петрович')
        

if __name__=='__main__':
        while True:
                try:
                        bot.infinity_polling(timeout=30, long_polling_timeout = 5)   
                except Exception as e:
                        time.sleep(3) 
                        print(e)
#bot.polling( non_stop = True)