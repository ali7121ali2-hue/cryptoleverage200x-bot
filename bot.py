import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📊 مميزات القناة", callback_data="features"),
        types.InlineKeyboardButton("💎 أسعار الاشتراك", callback_data="prices"),
        types.InlineKeyboardButton("💳 الدفع", callback_data="payment"),
        types.InlineKeyboardButton("📈 نتائج التوصيات", callback_data="results"),
        types.InlineKeyboardButton("🔐 قناة VIP", callback_data="vip"),
        types.InlineKeyboardButton("📞 التواصل", callback_data="contact")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
🔥 ما الذي يقدمه هذا البوت؟ 🔥

أهلاً بكم مع cryptoleverage200X Bot ❤️

📊 قناة متخصصة في تحليل العملات الرقمية.
📈 تحليل فني مميز من كبار المحللين وحيتان السوق.
💰 انضم إلى cryptoleverage200X وابدأ جني الأرباح.

🚀 بإذن الله كل أسبوع تدبيل من 2 أضعاف إلى 4 أضعاف.

📈 قناة نتائج وردود المشتركين:
https://t.me/Crypto_Leveragee125X

📞 حساب الدعم الفني:
https://t.me/ABBE_VIP2

👇 اختر من القائمة التالية:
""", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "features":
        text = "📊 مميزات القناة\n\n✅ توصيات صباحية ومسائية\n✅ سبوت وفيوتشر\n✅ قناة تعليمية\n✅ متابعة خاصة خطوة بخطوة\n\nللتواصل:\nhttps://t.me/ABBE_VIP2"
    elif call.data == "prices":
        text = "💎 أسعار الاشتراك\n\n🔹 اشتراك شهري = 30$\n🔹 شهرين = 60$\n🔹 3 أشهر = 80$\n🔹 سنوي = 200$"
    elif call.data == "payment":
        text = "💰 الدفع عبر USDT\n\n🌐 الشبكة: TRC20\n\n📍 عنوان المحفظة:\nTG8jzktMF9kR8hd6NDt3caiEbyXuoMpCqu\n\n📸 بعد التحويل أرسل صورة التحويل:\nhttps://t.me/ABBE_VIP2"
    elif call.data == "results":
        text = "📈 نتائج التوصيات:\n\nhttps://t.me/Crypto_Leveragee125X"
    elif call.data == "vip":
        text = "🔐 قناة VIP:\n\nhttps://t.me/+Vj79gCEYPBBkM2Y0"
    else:
        text = "📞 التواصل:\n\nhttps://t.me/ABBE_VIP2"

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, text, reply_markup=main_menu())
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_bot():
    bot.infinity_polling(skip_pending=True)

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
