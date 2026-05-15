import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)

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

def handle_message(update: Update, context: CallbackContext):
    msg = update.message
    if not msg or not msg.text:
        return
    text = msg.text
    if "BULLISH PULLBACK ENTRY" in text:
        msg.reply_text(BULLISH_REPLY)
    elif "BEARISH PULLBACK ENTRY" in text:
        msg.reply_text(BEARISH_REPLY)

def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    print("✅ Bot chal raha hai...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
