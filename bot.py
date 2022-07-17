
"""
Launch the bot
"""

from aiogram import executor
from dispatcher import dp
from handlers.personal_actions import set_default_commands
import handlers

async def on_startup(dispatcher):
	"""When bot is started, calls the method that sets default commands for user"""

	# set default commands
	await set_default_commands(dispatcher)

# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
