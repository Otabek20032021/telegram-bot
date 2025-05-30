
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7951523766:AAFgK90sv6n8OQBIegpGKCO7-Ys82YzS5ac"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Salom, {user.full_name}! Siz menga savol yuborishingiz mumkin."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    # Bu yerda foydalanuvchidan kelgan savolni qabul qilamiz
    await update.message.reply_text(
        "Xabaringiz adminlarga yetkazildi. Tez orada javob olasiz."
    )
    # Bu yerda kerak bo'lsa adminlarga xabar yuborish kodi qo'shish mumkin

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot ishga tushdi...")
    app.run_polling()
