import telebot
import os
import links as ln
from telebot import types
from telebot.util import quick_markup
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = os.getenv(
    'TELEGRAM_TOKEN', '1234:abcdefg'
)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome = f'Привет, {message.from_user.first_name} {message.from_user.last_name}, куда хотите пойти?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    attractions = types.KeyboardButton('/Достопримечательности')
    restaurants_and_bars = types.KeyboardButton('/Рестораны_и_бары')
    cultural_centers = types.KeyboardButton('/Культурные_центры')
    shop_mall = types.KeyboardButton('/ТЦ')
    excurs = types.KeyboardButton('/Экскурсии')
    worry = types.KeyboardButton('/Никуда_не_пойду_там_дождь')

    markup.add(
        attractions, restaurants_and_bars, cultural_centers, shop_mall, excurs, worry
        )
    bot.send_message(message.chat.id, welcome, reply_markup=markup)


@bot.message_handler(commands=['Достопримечательности'])
def attractions(message):
    text_attr = ('Северная столица, Город на Неве, Ленинград, Санкт-Петербург, Питер'
    ' — у него много имен, а народной любви ещё больше. Санкт-Петербург'
    ' всегда был вторым городом России, но для многих россиян и гостей из-за рубежа'
    ' он навсегда занял первое место в сердце.')
    markup_attr = quick_markup({
        'Эрмитаж': {'url': ln.HERMITAG},
        'Русский музей': {'url': ln.RUS_MUS},
        'Музей Фаберже': {'url': ln.FABERGE},
        'Исаакиевский собор': {'url': ln.CATH},
        'Юсуповский дворец': {'url': ln.YUSUPOV_PAL},
        'Петропавловская крепость': {'url': ln.PETR_PAVL},
        'Стрелка Васильевского острова': {'url': ln.ARROW},
        'Мариинский театр': {'url': ln.MAR_THEATRE},
        'Еще музеи...': {'url': ln.MUS_ALL},
        'Еще достопримечательности...': {'url': ln.ATTR_ALL}
    }, row_width=1)
    bot.send_message(message.chat.id, text_attr, reply_markup=markup_attr)


@bot.message_handler(commands=['Рестораны_и_бары'])
def rest_and_bars(message):
    text_rest = ('Самая вкусная еда таит в себе маленький секрет...'
                 ' в нее бросают всегда щепоточку любви.')
    markup_rest = quick_markup({
        'В Питере - ПИТЬ!': {'url': ln.DRINKS},
        'В Питере - есть шаверму!': {'url': ln.SHAVERMA},
        'Попробовать корюшку!': {'url': ln.SMELT},
        'Ленинградские пышки': {'url': ln.DON},
        'Лучшие рестораны СПб': {'url': ln.BEST_REST},
        'Видовые рестораны': {'url': ln.PANORAMIC}
    }, row_width=1)
    bot.send_message(message.chat.id, text_rest, reply_markup=markup_rest)


@bot.message_handler(commands=['Культурные_центры'])
def cul_cen(message):
    text_culcen = ('Счастье мое, доставай свой старый путеводитель,'
                   ' я знаю, город любви не Париж, а дождливый Питер...')
    markup_culcen = quick_markup({
        'Севкабель Порт': {'url': ln.SEVKABEL},
        'Новая Голландия': {'url': ln.NEW_HOLLAND},
        'Брусницын': {'url': ln.BRUSNITSIN}
    }, row_width=1)
    bot.send_message(message.chat.id, text_culcen, reply_markup=markup_culcen)


@bot.message_handler(commands=['ТЦ'])
def cul_cen(message):
    text_sm = ('ТЦ - хороший вариант досуга в СПб, если зимой - холодно и дожди,'
               ' летом - душно и дожди, или если дожди :)'
               '\nСамый большой торговый центр Питера - ТРЦ Галерея, яркий, современный,'
               ' расположенный в самом центре города.')
    markup_sm = quick_markup({
        'Галерея': {'url': ln.GALLERY},
        'Европолис': {'url': ln.EUROPOLIS},
        'Пассаж': {'url': ln.PASSAGE},
        'Лето': {'url': ln.SUMMER},
        'ПитерЛэнд': {'url': ln.PITERLAND},
        'Охта Молл': {'url': ln.OHTAMALL},
        'Все ТЦ Петербурга...': {'url': ln.SM_ALL}
    }, row_width=1)
    bot.send_message(message.chat.id, text_sm, reply_markup=markup_sm)


@bot.message_handler(commands=['Экскурсии'])
def cul_cen(message):
    text_exc = ('Петербург прекрасен всюду, но стоит увидеть красоты этого города'
               ' еще и с воды, высоты и изнури!'
               ' Поэтому предлагаю поплавать на корабликах - днем по каналам,'
               ' а ночью под разводными мостами.'
               ' И посетить экскурсию по крышам и дворам Петербурга.')
    markup_exc = quick_markup({
        'Экскурсии на корабликах': {'url': ln.BOATS},
        'По крышам Петербурга': {'url': ln.ROOFS},
        'Экскурсии по дворам Петербурга': {'url': ln.COURTYARDS},
        'Вертолетные экскурсии над городом': {'url': ln.HELICOPTERS},
        'Прогулка на двухэтажном автобусе': {'url': ln.BUSES}
    }, row_width=1)
    bot.send_message(message.chat.id, text_exc, reply_markup=markup_exc)


@bot.message_handler(commands=['Никуда_не_пойду_там_дождь'])
def cul_cen(message):
    text_rain = ('- А в петербурге давно дождь? \n'
               '- с 1703-го... \n'
               'Санкт-Петербург бесконечно кинематографичен. Это и уникальная натура,'
               '  и смыслообразующая декорация.'
               ' Многие великие истории могли произойти только здесь.')
    markup_rain = quick_markup({
        'Дворцы и трущобы: 10 фильмов о Петербурге': {'url': ln.COLLECTION1},
        'Подборка фильмов про СПб и Ленинград': {'url': ln.COLLECTION2},
        '10 фильмов про Петербург': {'url': ln.COLLECTION3},
        'Культурный гид по Санкт-Петербургу': {'url': ln.COLLECTION4}
    }, row_width=1)
    bot.send_message(message.chat.id, text_rain, reply_markup=markup_rain)

bot.polling(non_stop=True)