
import logging
import config
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# register '/start' and '/help' commands
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Handling '/start' and '/help'")

# echo function
@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)

# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
