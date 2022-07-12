
"""
Contains functions for creating keyboards
"""
from config import (
	UserMood, 
	Genre, 
	Show, 
	Novelty, 
	CustomReplyKeyboardButton,
	CustomInlineKeyboardButton
)
from aiogram.types import (
	ReplyKeyboardMarkup, 
	KeyboardButton, 
	InlineKeyboardMarkup, 
	InlineKeyboardButton
)

class KeyboardHandler():

	def get_main_replykeyboard():
		"""Sets up the main basic replykeyboard"""

		# replykeyboard btns
		smart_selection_btn = KeyboardButton(CustomReplyKeyboardButton.SMART_SELECTION_BTN.value)
		we_recommend_btn = KeyboardButton(CustomReplyKeyboardButton.WE_RECOMMEND_BTN.value)
		no_preferences_btn = KeyboardButton(CustomReplyKeyboardButton.NO_PREFERENCES_BTN.value)
		send_feedback_btn = KeyboardButton(CustomReplyKeyboardButton.SEND_FEEDBACK_BTN.value)

		return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
			.add(smart_selection_btn).add(we_recommend_btn).add(no_preferences_btn).add(send_feedback_btn)

	def get_mood_inlinekeyboard():
		"""Sets up inlinekeyboard for user's mood selection"""

		# inlinekeyboard btns
		depression_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.DEPRESSION_BTN.value, callback_data=UserMood.DEPRESSION.value)
		cheerful_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.CHEERFUL_BTN.value, callback_data=UserMood.CHEERFUL.value)
		whatever_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.WHATEVER_BTN.value, callback_data=UserMood.WHATEVER.value)
		lot_on_my_mind_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.LOT_ON_MY_MIND_BTN.value, callback_data=UserMood.LOT_ON_MY_MIND.value)
		stressed_out_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.STRESSED_OUT_BTN.value, callback_data=UserMood.STRESSED_OUT.value)
		no_strength_at_all_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.NO_STRENGTH_AT_ALL_BTN.value, callback_data=UserMood.NO_STRENGTH_AT_ALL.value)
		fighting_spirit_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.FIGHTING_SPIRIT_BTN.value, callback_data=UserMood.FIGHTING_SPIRIT.value)
		family_weekend_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.FAMILY_WEEKEND_BTN.value, callback_data=UserMood.FAMILY_WEEKEND.value)
		group_of_friends_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.GROUP_OF_FRIENDS_BTN.value, callback_data=UserMood.GROUP_OF_FRIENDS.value)
		love_btn = InlineKeyboardButton(text=CustomInlineKeyboardButton.LOVE_BTN.value, callback_data=UserMood.LOVE.value)
	
		return InlineKeyboardMarkup().add(depression_btn, cheerful_btn, whatever_btn, 
			lot_on_my_mind_btn, stressed_out_btn, no_strength_at_all_btn, fighting_spirit_btn, 
			family_weekend_btn, group_of_friends_btn, love_btn)