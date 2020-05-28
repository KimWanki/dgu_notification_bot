import crawl
# from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler

BOT_TOKEN = '1184167751:AAGpHJpcCxIz5IVof5oVq6oY4Mf9DEb-3Wg'

updater = Updater( token = BOT_TOKEN, use_context= True)
dispatcher = updater.dispatcher

def cmd_crawl(update, context):
    task_buttons = [[
        InlineKeyboardButton('학사공지', callback_data='dongguk_scholar')
        , InlineKeyboardButton('일반공지', callback_data='dongguk_normal')
    ], [
        InlineKeyboardButton('취소', callback_data='cancel')
    ]]

    reply_markup = InlineKeyboardMarkup(task_buttons)
    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='동국아, 무슨 공지를 볼래?'
        , reply_markup=reply_markup
    )


def cb_crawl(update, context):
    query = update.callback_query
    target = query.data

    if target == 'cancel':
        context.bot.edit_message_text(
            text='취소.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
    else:
        context.bot.edit_message_text(
            text='좀만 기다리쇼잉.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
        for item in crawl.run(target):
            print(item)
            context.bot.send_message(
                chat_id=update.effective_chat.id
                , text="공지명: {title}\n발행일:{date}\n{link}".format(title=item["title"], date=item["date"],
                                                                   link=item["link"])
            )
        context.bot.edit_message_text(
            text='됐다잉'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
crawl_handler = CommandHandler('dongguk', cmd_crawl)
crawl_cb_handler = CallbackQueryHandler(cb_crawl)

dispatcher.add_handler(crawl_handler)
dispatcher.add_handler(crawl_cb_handler)

updater.start_polling()
updater.idle()
