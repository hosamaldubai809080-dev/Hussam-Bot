import telebot
from telebot import types
from urllib.parse import quote

# إعدادات القيادة حسام الدبعي
TOKEN = "8295138919:AAETniTO5Z6pAuUkytOCPiTFh6s_5tjWaPA"
CHANNEL_ID = "-1003775083215" 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('ثغرة الإباحي 🔞')
    btn2 = types.KeyboardButton('قسم الطعن ⚖️')
    btn3 = types.KeyboardButton('قسم التخمين 🛡️')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "مرحباً يا قيادة حسام. اختر القسم لبدء العملية:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['ثغرة الإباحي 🔞', 'قسم الطعن ⚖️', 'قسم التخمين 🛡️'])
def ask_for_number(message):
    category = message.text
    msg = bot.send_message(message.chat.id, f"🎯 أرسل الرقم المستهدف لقسم [{category}]:")
    bot.register_next_step_handler(msg, execute_operation, category)

def execute_operation(message, category):
    target = message.text
    report = f"📢 [تقرير عملية]\n👤 القائد: حسام الدبعي\n🎯 الهدف: {target}\n📂 القسم: {category}"
    bot.send_message(CHANNEL_ID, report) # النشر التلقائي في القناة
    
    subject = quote(f"Audit: {target}")
    body = quote(f"App: com.whatsapp\nTarget: {target}\nViolation: {category}")
    mail_url = f"mailto:support@support.whatsapp.com?subject={subject}&body={body}"
    
    bot.send_message(message.chat.id, f"✅ تم التوثيق بالقناة.\n🚀 [اضغط هنا للإرسال للمقر]({mail_url})", parse_mode="Markdown")

bot.polling(none_stop=True)
