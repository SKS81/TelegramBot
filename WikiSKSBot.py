# pip install wikipedia

import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot('   ')
wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'Либо этого там ещё нет, либо у этого несколько отдельных страниц с разными определениями. Для перехода на сайт Википедии нажмите на кнопку Сайт Википедия внизу слева и поищите там)))'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я - ВикиСКС-БОТ. Напиши что-нибудь и я попробую найти определение этого в Википедии.)))')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton("/start")
    markup.add(item)
    bot.send_message(m.chat.id, 'Нажми в самом низу \nкнопку /start для повторного прочтения приветствия', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)