from telebot.types import Message, ReplyKeyboardMarkup
from config import TOKEN
import telebot
import random

bot = telebot.TeleBot(TOKEN)
resources = ["Золото", "старый ключ", "рунный камень", "меч героя", "голова змея", "арбалет", "лук старого эльфа",
             "часы", "кольцо", "цепочка королевы", "ржавая монета", "кости", "старая кукла", "дух воина",
             "серп жителя земель", "платок дамы", "лампа", "солнце защитные очки", "шляпа торговца", "шлем гладиатора"]
temp = {}


@bot.message_handler(['start'])
def start(m: Message):
    try:
        print(temp[m.chat.id])
        print(temp)
    except:
        temp[m.chat.id] = {}

    kb = ReplyKeyboardMarkup(resize_keyboard=False)
    kb.row("КОПАТЬ")
    bot.send_message(m.chat.id,
                     text="привет ты в игре яблочко здесь ты можешь копать, и получать промокоды с вероятностью в 5%",
                     reply_markup=kb)


@bot.message_handler(content_types=["text"])
def text(m: Message):
    if m.text == "КОПАТЬ":
        try:
            print(temp[m.chat.id]["promo"])
            print(temp)
        except:
            temp[m.chat.id]["promo"] = False
        res = random.choice(resources)
        promo = random.randint(1, 100)
        print(promo)
        bot.send_message(m.chat.id, text=f"ты получил случайный ресурс из ящика Пандоры: {res}")
        if promo in range(1, 6):
            if temp[m.chat.id]["promo"] is False:
                bot.send_message(m.chat.id, text=f"ты получил промо код для покупок!")
                bot.send_message(m.chat.id, text="Super_Promo2023")
                temp[m.chat.id]["promo"] = True


bot.infinity_polling()
