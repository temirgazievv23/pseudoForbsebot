import telebot
from telebot import types

bot = telebot.TeleBot(Bot_Token)


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hi! Type or click.")
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Statistics', 'Schedule')
    keyboard.row('Reshuffle', 'About bot')
    bot.send_message(m.chat.id,
                     'You\'ve got your options!',
                     reply_markup=keyboard)


@bot.message_handler(commands=["links"])
def links(m):
    msg = bot.send_message(m.chat.id,
                           "Here are the links that might be useful:")
    bot.send_message(m.chat.id, '''[HLTV](https://www.hltv.org/team/4608/natus-vincere)
[Instagram](https://www.instagram.com/natus_vincere_official/)
[YouTube](https://www.youtube.com/c/navicsgo/featured)
[Twitter](https://twitter.com/natusvincere?lang=ru)
[Facebook](https://www.facebook.com/NatusVincere/)
[NaVi official website](https://navi.gg/en/)
    ''', parse_mode='Markdown')


@bot.message_handler(commands=["events"])
def links(m):
    bot.send_message(m.chat.id,
                     'Ongoing events: ')
    bot.send_message(m.chat.id,
                     '[EM Beijing-Haidian 2020 Europe]'
                     '(https://www.hltv.org'
                     '/events/5524/'
                     'iem-beijing-haidian-2020-europe)\n'
                     '[BLAST Premier Fall 2020 Finals]'
                     '(https://www.hltv.org/events'
                     '/5209/blast-premier-fall-2020-finals)',
                     parse_mode='Markdown')
    bot.send_photo(m.chat.id,
                   'http://prntscr.com/ve19id.png')
    bot.send_photo(m.chat.id,
                   'http://prntscr.com/ve19vg.png')


@bot.message_handler(content_types=['text'])
def blabla(m):
    if m.text.lower() == 'main menu':
        msg = bot.send_message(m.chat.id,
                               "Alright, what are we going to be up to?")
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Statistics', 'Schedule')
        keyboard.row('Reshuffle', 'About bot')
        bot.send_message(m.chat.id, 'You\'ve got your options!',
                         reply_markup=keyboard)

    elif m.text.lower() == 'reshuffle':
        bot.send_message(m.chat.id, , parse_mode='Markdown')
        bot.send_message(m.chat.id, , parse_mode='Markdown')
        bot.send_message(m.chat.id, ,parse_mode='Markdown')

    elif m.text.lower() == 'about bot':
        bot.send_message(m.chat.id,
                         'This bot is made by a freshman '
                         'for a university project. '
                         'It does nothing special, '
                         'basically it just gives some '
                         'scripted information you ask for, '
                         'but might be useful if you'
                         ' want to quickly know who is the richest person in the world.')
    elif m.text.lower() == 'statistics':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('s1mple')
        keyboard.row('flamie', 'Boombl4')
        keyboard.row('Perfecto', 'electronic')
        keyboard.row('Main menu')
        bot.send_message(m.chat.id,
                         'Choose a player you want to know statistics of',
                         reply_markup=keyboard)


    else:
        bot.send_message(m.chat.id,
                         'Please, enter something valid '
                         'or use a integrated Telegram keyboard')

bot.polling(none_stop=True)
