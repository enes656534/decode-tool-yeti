import telebot
import random
from faker import Faker
import os
import time

token = "6838301588:AAGAcjdFdKj1XDKGJ7zxp229AgctwuZeVws"
bot = telebot.TeleBot(token)
time.sleep(2)
os.system('clear')
print("Bot'a /start yaz")

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, """Merhabalar botu kullanmak için @YeniHack24 ve @PythonDeposu kanalına katılman gerekmektedir
-----------------------------
Katıldıysan kullanabilirsin
-----------------------------
Api biraz yavaş olabilir
-----------------------------
Komutum; /vds - rastgele vds oluşturur ve kontrol eder
-----------------------------
Not: Live Vds Leri Kullanabilirsiniz
-----------------------------
Kurucular @YENI_HACK ve @Yeticik""")

@bot.message_handler(commands=["vds"])
def vds(msg):
    vds = vds_yenihack()
    ip = vds["ip"]
    username = vds["user"]
    password = vds["passwrd"]
    is_live = check_vds(ip)
    if is_live:
        bot.reply_to(msg, f"LIVE VDS ✅\nIP: {ip}\nUsername: {username}\nPassword: {password}")
    else:
        bot.reply_to(msg, f"DEC VDS ❌\nIP: {ip}\nUsername: {username}\nPassword: {password}")

def vds_yenihack():
    return {"ip": f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}", "user": "Administrator", "passwrd": Faker("tr_TR").password()}

def check_vds(ip):
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    else:
        return False

bot.polling()
