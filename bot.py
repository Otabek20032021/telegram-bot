
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7951523766:AAFgK90sv6n8OQBIegpGKCO7-Ys82YzS5ac"
ADMIN_ID = 678347563  # Sizning Telegram user ID'ingiz

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Savolingizni yozing, men adminga yetkazaman.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    await context.bot.send_message(chat_id=ADMIN_ID,
                                   text=f"Foydalanuvchi @{user.username} (ID: {user.id}) dan xabar:\n\n{text}")

    await update.message.reply_text("Xabar adminga yetkazildi. Rahmat!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
