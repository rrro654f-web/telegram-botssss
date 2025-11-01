import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не знайдено!")
    sys.exit(1)

WELCOME_TEXT = """🎉 Ласкаво просимо до нашого магазину!"""

GIF_URL = "https://i.gifer.com/3P0Ho.gif"
WEB_APP_URL = "https://itconcerent.github.io/markesell/"

def start(update: Update, context: CallbackContext) -> None:
    try:
        keyboard = [[
            InlineKeyboardButton(
                "🛍️ Відкрити магазин", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        update.message.reply_animation(
            animation=GIF_URL,
            caption=WELCOME_TEXT,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    except Exception as e:
        logger.error(f"Помилка: {e}")

def main() -> None:
    try:
        updater = Updater(BOT_TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        
        logger.info("🤖 Бот запускається...")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ Помилка запуску: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
