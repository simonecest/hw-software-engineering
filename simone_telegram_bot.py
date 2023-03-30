import telebot

bot=telebot.TeleBot('5820162074:AAFpb_CnUg68pbhcv_qbbVOPDHXxtvpm4dw')

@bot.message_handler(commands=['hi','hello'])
def send_welcome(message):
    bot.reply_to(message,'how u doing')

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()