import telebot
from telebot import types

bot = telebot.TeleBot('1441937797:AAH4yb0pEysU9Rm_HBolmP6owKK8aiRFkWM')


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hi! Type or click.")
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('World\'s Billionaires', 'Richest Women')
    keyboard.row('Wealthiest sportsmen', 'About bot')
    bot.send_message(m.chat.id,
                     'You\'ve got your options!',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def mainmen(m):
    if m.text.lower() == 'main menu':
        msg = bot.send_message(m.chat.id,
                               "Alright, what are we going to be up to?")
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('World\'s Billionaires', 'Richest Women')
        keyboard.row('Wealthiest sportsmen', 'About bot')
        bot.send_message(m.chat.id, 'You\'ve got your options!',
                         reply_markup=keyboard)

    elif m.text.lower() == 'richest women':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Alice Walton', 'Francoise B. Meyers', 'Mackenzie Bezos')
        keyboard.row('Jacqueline Mars', 'Yang Huiyan', 'Julia Koch')
        keyboard.row('Susanne Klatten', 'Laurene Powell', 'Zhong Huizuan')
        keyboard.row('Main menu', 'Gina Rinehart')
        bot.send_message(m.chat.id,
                         '''1. *Alice Walton* $54.4B 
2. *Francoise Bettencourt Meyers & family* $48.9B
3. *Julia Koch* $38.2B
4. *Mackenzie Bezos* $36B
5. *Jacqueline Mars* $24.7B
6. *Yang Huiyan* $20.3B
7. *Susanne Klatten* $16.8B
8. *Laurene Powell* $16.4B
9. *Zhong Huizuan* $14.6B
10. *Gina Rinehart* $13.1B

    _Note: information provided in screenshots (net-worth, age, etc.) may be no more actual, but what is written, is the newest._''',
                         parse_mode='Markdown', reply_markup=keyboard)
    elif m.text.lower() == 'alice walton':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12jz3.png')
        bot.send_message(m.chat.id,
                         '''Age *71*
Source of wealth [Walmart](https://www.walmart.com)
Self-made score *1*
Philantrophy score *2*
Residence *Fort Worth, Texas*
Citizenship *USA*
Education *Bachelor of Arts/Science, Trinity University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'francoise b. meyers':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12l17.png')
        bot.send_message(m.chat.id,
                         '''Age *67*
Source of wealth [L'Oreal](https://www.loreal.com/fr/)
Residence *Paris, France*
Citizenship *France*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'julia koch':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12lxh.png')
        bot.send_message(m.chat.id,
                         '''Age *58*
Source of wealth [Koch Industries](https://www.kochind.com)
Self-made score *1*
Philantrophy score *2*
Residence *New York*
Citizenship *USA*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'mackenzie bezos':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12mhx.png')
        bot.send_message(m.chat.id,
                         '''Age *50*
Source of wealth [Amazon](https://www.amazon.com)
Self-made score *3*
Philantrophy score *2*
Residence *Seattle, Washington*
Citizenship *USA*
Education *Bachelor of Arts/Science, Princeton University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'jacqueline mars':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12n3l.png')
        bot.send_message(m.chat.id,
                         '''Age *81*
Source of wealth *candy, pet food*
Self-made score *2*
Residence *The Plains, Virginia*
Citizenship *USA*
Education *Bachelor of Arts/Science, Bryn Mawr College*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'yang huiyan':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12np2.png')
        bot.send_message(m.chat.id,
                         '''Age *39*
Source of wealth *real estate*
Residence *Foshan, China*
Citizenship *China*
Education *Bachelor of Arts/Science, Ohio State University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'susanne klatten':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12oct.png')
        bot.send_message(m.chat.id,
                         '''Age *58*
Source of wealth [BMW](https://www.bmw.com/de), *pharmaceuticals*
Residence *Bad Homburg, Germany*
Citizenship *Germany*
Education *Master of Business Administration, 
International Institute for Management and Development*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'laurene powell':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12p5e.png')
        bot.send_message(m.chat.id,
                         '''Age *57*
Source of wealth [Apple](https://www.apple.com), [Disney](https://www.disney.com)
Self-made score *2*
Philantrophy score *1*
Residence *Palo Alto, California*
Citizenship *USA*
Education *Master of Business Administration, Stanford Graduate School of Business; 
Bachelor of Arts/Science, University of Pennsylvania, The Wharton School*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'zhong huizuan':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12q2x.png')
        bot.send_message(m.chat.id,
                         '''Age *59*
Source of wealth *pharmaceuticals, Self Made*
Residence *Shanghai, China*
Citizenship *China*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'gina rinehart':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12qn0.png')
        bot.send_message(m.chat.id,
                         '''Age *66*
Source of wealth *mining*
Residence *Perth, Australia*
Citizenship *Australia*''',
                         parse_mode='Markdown')

    elif m.text.lower() == 'world\'s billionaires':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Jeff Bezos', 'Sergey Brin', 'Bill Gates')
        keyboard.row('Mark Zuckerberg', 'Elon Musk', 'Bernard Arnault & family')
        keyboard.row('Warren Buffet', 'Larry Elisson', 'Larry Page', 'Mukesh Ambani')
        keyboard.row('Main menu')
        bot.send_message(m.chat.id,
                         '''1. [Jeff Bezos](https://www.forbes.com/profile/jeff-bezos/?list=rtb/&sh=512e93ce1b23) *$182.2B* 
2. [Bernard Arnault & family](https://www.forbes.com/profile/bernard-arnault/?list=rtb/&sh=23f26c4e66fa) *$146.5B*
3. [Elon Musk](https://www.forbes.com/profile/elon-musk/?list=rtb/&sh=7752702e7999) *$136.9B*
4. [Bill Gates](https://www.forbes.com/profile/bill-gates/?list=rtb/&sh=50c27be9689f) *$118.8B*
5. [Mark Zuckergerg](https://www.forbes.com/profile/mark-zuckerberg/?list=rtb/&sh=758286c93e06) *$100.5B*
6. [Waren Buffet](https://www.forbes.com/profile/warren-buffett/?list=rtb/&sh=791294d04639) *$86.6B*
7. [Larry Elisson](https://www.forbes.com/profile/larry-ellison/?list=rtb/&sh=3f92999924c2) *$82.4B*
8. [Larry Page](https://www.forbes.com/profile/larry-page/?list=rtb/&sh=3bf29df57893) *$78.3B*
9. [Mukesh Ambani](https://www.forbes.com/profile/mukesh-ambani/?list=rtb/&sh=68a34c11214c) *$76.4B*
10. [Sergei Brin](https://www.forbes.com/profile/sergey-brin/?list=rtb/&sh=582353824b43) *$76.0B*''',
                         parse_mode='Markdown', reply_markup=keyboard)
        bot.send_message(m.chat.id,
                         '_Note: Names are clickable, press them to go to the one\'s Forbes profile_',
                         parse_mode='Markdown')
    elif m.text.lower() == 'jeff bezos':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w124x7.png')
        bot.send_message(m.chat.id,
                         '''Age *56*
Source of wealth *Amazon, Self made*
Self-made score, *8*
Residence *Seattle, Washington*
Citizenship *USA*
Education *Bachelor or Arts/Science, Princeton University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'bernard arnault & family':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12799.png')
        bot.send_message(m.chat.id,
                         '''Age *71*
Source of wealth *Moët Hennessy — Louis Vuitton*
Residence *Paris, France*
Citizenship *France*
Education *Bachelor or Arts/Science, Ecole Polytechnique de Paris*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'elon musk':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w1288x.png')
        bot.send_message(m.chat.id,
                         '''Age *49*
Source of wealth *Tesla, SpaceX, Self Made*
Self-made score, *8*
Residence *Austin, Texas*
Citizenship *USA*
Education *Bachelor or Arts/Science, University of Pennsylvania*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'bill gates':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w1297f.png')
        bot.send_message(m.chat.id,
                         '''Age *65*
Source of wealth *Microsoft, Self made*
Self-made score, *8*
Residence *Medina, Washington*
Citizenship *USA*
Education *Drop out, Harvard University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'mark zuckerberg':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w129sn.png')
        bot.send_message(m.chat.id,
                         '''Age *36*
Source of wealth *Facebook, Self made*
Self-made score, *8*
Residence *Palo Alto, California*
Citizenship *USA*
Education *Drop out, Harvard University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'warren buffet':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12aet.png')
        bot.send_message(m.chat.id,
                         '''Age *90*
Source of wealth *Berkshire Hathaway, Self Made*
Self-made score, *8*
Residence *Omaha, Nebraska*
Citizenship *USA*
Education *Bachelor of Arts/Science, University 
of Nebraska Lincoln; Master of Science, Columbia University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'larry elisson':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12bd4.png')
        bot.send_message(m.chat.id,
                         '''Age *76*
Source of wealth *software, Self Made*
Self-made score, *8*
Residence *Woodside, California*
Citizenship *USA*
Education *Drop Out, University of Chicago; 
Drop Out, University of Illinois, Urbana-Champaign*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'larry page':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12c4e.png')
        bot.send_message(m.chat.id,
                         '''Age *47*
Source of wealth *Google, Self Made*
Self-made score, *8*
Residence *Palo Alto, California*
Citizenship *USA*
Education *Bachelor of Arts/Science, University of Michigan; 
Master of Science, Stanford University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'mukesh ambani':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12civ.png')
        bot.send_message(m.chat.id,
                         '''Age *63*
Source of wealth *diversified*
Residence *Mumbai, India*
Citizenship *India*
Education *Bachelor of Science in Engineering, University of Bombay; 
Drop Out, Stanford University*''',
                         parse_mode='Markdown')
    elif m.text.lower() == 'sergey brin':
        bot.send_photo(m.chat.id, 'http://prntscr.com/w12dcz.png')
        bot.send_message(m.chat.id,
                         '''Age *47*
Source of wealth *Google, Self Made*
Self-made score, *9*
Residence *Los Altos, California*
Citizenship *USA*
Education *Master of Science, Stanford University; 
Bachelor of Arts/Science, University of Maryland, College Park*''',
                         parse_mode='Markdown')

    elif m.text.lower() == 'wealthiest sportsmen':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Tennis')
        keyboard.row('Box', 'Soccer')
        keyboard.row('Basketball', 'Golf')
        keyboard.row('Main menu')
        bot.send_message(m.chat.id,
                         'The 100 highest-paid athletes earned a combined'
                         ' $3.6 billion this year, which is 9% below 2019.\n'
                         'Now, choose a kind of sport.',
                         reply_markup=keyboard)
    elif m.text.lower() == 'tennis':
        bot.send_message(m.chat.id,
                         '''1. *Roger Federer* $450M
2. *Novak Djokovic* $220M
3. *Serena Williams* $200M
4. *Rafael Nadal* $180M
5. *Andy Murray* $165M
6. *Maria Sharapova* $135$
7. *Venus Williams* $95M
8. *Simona Halep* $30M
9. *Angelique Kerber* $30M
10. *Caroline Wozniacki* $30M''',
                         parse_mode='Markdown')
        bot.send_message(m.chat.id,
                         'Tennis is definitely the biggest non-team sport, '
                         'and with over a billion fans in the world today, '
                         'it is one of the world’s biggest sports. '
                         'The ranking is primarily based on the '
                         'net worths of currently active players, '
                         'or at least players who had not retired before January 2020.',
                         parse_mode='Markdown')
    elif m.text.lower() == 'box':
        bot.send_message(m.chat.id,
                         '''1. *Floyd Mayweather* $450M
2. *George Foreman* $400M
3. *Manny Pacquiao* $220M
4. *Oscar De La Hoya* $200M
5. *Don King * $150M
6. *Lennox Lewis* $140M
7. *Saul Alvarez* $140M
8. *Sugar Ray Leonard* $120M
9. *Wladimir Klitschko* $90M
10. *Anthony Joshua* $80M''',
                         parse_mode='Markdown')
        bot.send_message(m.chat.id, 'The ranking is primarily based on the ' 
                         'net worths of players of all time.',
                         parse_mode='Markdown')
    elif m.text.lower() == 'football':
        bot.send_message(m.chat.id,
                         '''1. *Lionel Messi, Barcelona* $126M
2. *Cristiano Ronaldo, Juventus* $117M
3. *Neymar Jr, PSG* $96M
4. *Kylian Mbappe, PSG* $42M
5. *Mohammed Salah, Liverpool* $37M
6. *Paul Pogba, Manchester United* $34M
7. *Antoine Griezmann, Barcelona* $33M
8. *Gareth Bale, Tottenham* $29M
9. *Robert Lewandowski, Bayern M.* $28M
10. *David de Gea, Manchester United* $27M''',
                         parse_mode='Markdown')
        bot.send_message(m.chat.id, 'The ranking is primarily based on the' 
                         'players\' salaries paid by their clubs, '
                         'not including external contracts and business projects.',
                         parse_mode='Markdown')
    elif m.text.lower() == 'golf':
        bot.send_message(m.chat.id,
                         '''1. *Tiger Woods* $800M
2. *Arnold Palmer* $700M
3. *Phil Mickelson* $400M
4. *Jack Nicklaus* $320M
5. *Greg Norman* $300M
6. *Gary Player* $250M
7. *Rory Mcilroy* $130M
8. *Fred Couples* $120M
9. *Jordan Spieth* $100M
10. *Ernie Els* $85M''',
                         parse_mode='Markdown')
        bot.send_message(m.chat.id, 'The ranking is primarily based on the ' 
                         'net worths of players of all time.',
                         parse_mode='Markdown')
    elif m.text.lower() == 'basketball':
        bot.send_message(m.chat.id,
                         '''1. *Michael Jordan* $1.5B
2. *Junior Bridgeman* $600M
3. *Magic Johnson* $600M
4. *Lebron James* $440M
5. *Shaquelle O'Neal* $410M
6. *Kobe Bryant* $350M
7. *David Robinson* $200M
8. *Hakeem Olajuwon* $200M
9. *Kevin Garnett* $190M
10. *Grant Hill* $180M''',
                         parse_mode='Markdown')
        bot.send_message(m.chat.id, 'The ranking is primarily based on the ' 
                         'net worths of players.',
                         parse_mode='Markdown')

    elif m.text.lower() == 'about bot':
        bot.send_message(m.chat.id,
                         'This bot is made by a freshman '
                         'for a university project. '
                         'It does nothing special, '
                         'basically it just gives some '
                         'scripted information you ask for, '
                         'but might be useful if you'
                         ' want to quickly know who is the richest person in the world.')

    else:
        bot.send_message(m.chat.id,
                         'Please, enter something valid '
                         'or use a integrated Telegram keyboard')


bot.polling(none_stop=True)


