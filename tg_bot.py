import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext

from dialogflow import detect_intent_text


logging.basicConfig(
    filename=f'{__file__.replace(".py", "")}.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def reply_to_user(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    reply_text, _ = detect_intent_text(
        env.str('GOOGLE_CLOUD_PROJECT_ID'),
        update.message.chat_id,
        text
    )

    update.message.reply_text(reply_text)


if __name__ == '__main__':
    env = Env()
    env.read_env()

    tg_bot_token = env.str('TG_BOT_TOKEN')

    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, reply_to_user
    ))

    updater.start_polling()
    updater.idle()
