
"""
Handle events when clicking on buttons
Buttons themselves are stored in 'personal_actions', only their callbacks are processed here
"""

from aiogram import types
from dispatcher import dp
from config import UserMood
import config

# @dp.callback_query_handler(text=UserMood.list())
# async def process_mood(call: types.CallbackQuery):
# 	