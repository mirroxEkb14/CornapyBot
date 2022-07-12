
"""
Launch the bot
"""

from aiogram import executor
from dispatcher import dp
import handlers

# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
