import telebot

BOT_TOKEN = "ضع_توكن_البوت_هنا"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا روبوت التعليم، كيف يمكنني مساعدتك اليوم؟")

print("البوت يعمل الآن بنجاح...")
bot.infinity_polling()
8785413841:AAGis_NOSU2x97NNzEUHN-KCEL-PDqtKnO8

