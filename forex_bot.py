from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ⚠️ APNA NAYA TOKEN YAHAN DAALO
BOT_TOKEN = "8773153425:AAGUnnJym4lgVjRL2DP0nL2lN76ZCdevv_A"

BULLISH_REPLY = (
    "How to enter: Wait for the Fractal to form. "
    "Ensure candles are trading above the EMAs. "
    "Place a Buy Stop at the Fractal High, and set your Stop Loss at the candle's low."
)

BEARISH_REPLY = (
    "How to enter: Wait for the Fractal to form. "
    "Ensure candles are trading below the EMAs. "
    "Place a Sell Stop at the Fractal Low, and set your Stop Loss at the candle's high."
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    text = msg.text

    # Bullish alert check
    if "BULLISH PULLBACK ENTRY" in text:
        await msg.reply_text(BULLISH_REPLY)

    # Bearish alert check
    elif "BEARISH PULLBACK ENTRY" in text:
        await msg.reply_text(BEARISH_REPLY)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot chal raha hai... (Ctrl+C se band karo)")
    app.run_polling()

if __name__ == "__main__":
    main()
