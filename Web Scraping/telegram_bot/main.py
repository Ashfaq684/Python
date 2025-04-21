from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN: Final = '6402854565:AAG8gaZ26vALNtYYPhzqkC2DuTNyutQhVck'
BOT_USERNAME: Final = '@bbanana_64_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a banana')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a banana! Please type something so I can respond!')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')


# responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    
    return 'I do not understand what you wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_message(new_text)
        else:
            return
    else:
        respone: str = handle_response(text)
    
    print('Bot:', respone)
    await update.message.reply_text(respone)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error "{context.error}"')


if __name__ == '__main__':
    print('Starting Python Bot...')
    application = Application.builder().token(TOKEN).build()
    
    # commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('custom', custom_command))
    
    # messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # errors
    application.add_error_handler(error)
    
    # run
    print('Polling...')
    application.run_polling(poll_interval=3)