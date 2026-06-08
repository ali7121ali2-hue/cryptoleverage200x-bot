import os
import threading
from flask import Flask
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
VIP_CHANNEL = int(os.getenv("VIP_CHANNEL"))

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📊 مميزات القناة", callback_data="features"),
        types.InlineKeyboardButton("💎 أسعار الاشتراك", callback_data="prices"),
        types.InlineKeyboardButton("💳 الدفع", callback_data="payment"),
        types.InlineKeyboardButton("📈 نتائج التوصيات", callback_data="results"),
        
        types.InlineKeyboardButton("📞 التواصل", callback_data="contact")
    )
    return markup

@bot.message_handler(commands=["start"])
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
    if call.data.startswith("approve_"):
        user_id = int(call.data.replace("approve_", ""))

        invite = bot.create_chat_invite_link(
            chat_id=VIP_CHANNEL,
            name=f"user_{user_id}",
            member_limit=1
        )

        bot.send_message(
            user_id,
            f"✅ تم قبول اشتراكك بنجاح.\n\n🔐 رابط دخول VIP الخاص بك:\n{invite.invite_link}\n\n⚠️ الرابط صالح لاستخدام واحد فقط."
        )

        bot.answer_callback_query(call.id, "تم قبول الاشتراك")
        return

    if call.data.startswith("reject_"):
        user_id = int(call.data.replace("reject_", ""))

        bot.send_message(
            user_id,
            "❌ تم رفض إثبات الدفع.\n\n📞 تواصل مع الدعم:\nhttps://t.me/ABBE_VIP2"
        )

        bot.answer_callback_query(call.id, "تم رفض الطلب")
        return

if call.data == "features":
        text = "📊 مميزات القناة\n\n✅ توصيات صباحية ومسائية\n✅ سبوت وفيوتشر\n✅ قناة تعليمية\n✅ متابعة خاصة خطوة بخطوة"

    elif call.data == "prices":
        text = "💎 أسعار الاشتراك\n\n💎 شهر = 30$\n💎 3 أشهر = 80$\n💎 سنوي = 200$"

    elif call.data == "payment":
        text = "💰 الدفع عبر USDT\n\n🌐 الشبكة: TRC20"

    elif call.data == "results":
        text = "📈 نتائج التوصيات:\n\nhttps://t.me/Crypto_Leveragee125X"

    else:
        text = "📞 التواصل:\n\nhttps://t.me/ABBE_VIP2"

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=main_menu()
    )
@bot.message_handler(content_types=['photo'])
def handle_payment_proof(message):

    user_name = message.from_user.first_name

    username = message.from_user.username

    user_id = message.from_user.id

    caption = f"""
📥 إثبات دفع جديد

👤 الاسم: {user_name}

📱 اليوزر: @{username}

🆔 الآيدي: {user_id}
"""

    photo = message.photo[-1].file_id

    admin_buttons = types.InlineKeyboardMarkup()
    admin_buttons.add(
        types.InlineKeyboardButton("✅ قبول الاشتراك", callback_data=f"approve_{user_id}"),
        types.InlineKeyboardButton("❌ رفض الدفع", callback_data=f"reject_{user_id}")
    )

    bot.send_photo(
        ADMIN_ID,
        photo,
        caption=caption,
        reply_markup=admin_buttons
    )
    
def run_bot():
    print("Bot Started...")

    while True:
        try:
            bot.infinity_polling(skip_pending=True, timeout=10, long_polling_timeout=5)
        except Exception as e:
            print("Polling error:", e)
            import time
            time.sleep(10)
if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
