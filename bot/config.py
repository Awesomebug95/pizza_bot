from aiogram import Bot, Dispatcher

# Я не стал скрывать токен в .env,
# так как возможно вы захотите запустить бота.
TOKEN = "5005317041:AAFwtHn6HIn_dnGxCDy-SXIuTFZI4Wed0NE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
