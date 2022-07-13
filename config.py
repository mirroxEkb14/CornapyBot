
"""
Contains the config
"""

import os
from enum import Enum

# get environment variable
TOKEN = os.environ.get('BOT_TOKEN')

# user's selected mood, show type(movie/series), genre
USER_MOOD = None
USER_SHOW = None
USER_GENRE = None

class UserMood(Enum):
	DEPRESSION = 'depression'
	CHEERFUL = 'cheerful'
	DONT_KNOW = "don't know"
	LOT_ON_MY_MIND = 'lot on my mind'
	STRESSED_OUT = 'stressed out'
	NO_STRENGTH_AT_ALL = 'no strength at all'
	FIGHTING_SPIRIT = 'fighting spirit'
	FAMILY_WEEKEND = 'family weekend'
	GROUP_OF_FRIENDS = 'group of friends'
	LOVE = 'love'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))

class Genre(Enum):
	COMEDY = 'comedy'
	THRILLER = 'thriller'
	ACTION = 'action'
	DOCUMENTARY = 'documentary'
	FAMILY = 'family'
	SPORT = 'sport'
	FANTASY = 'fantasy'
	ANIMATION = 'animation'

class Show(Enum):
	"""What kind of show user wants to watch"""
	MOVIE = 'movies'
	SERIES = 'series'

class Novelty(Enum):
	"""
	Films before 2010 included are considered as old (upper bound)
	Films after 2010 are considered as modern (lower bound)
	"""
	OLD = 2010
	MODERN = 2011

class CustomReplyKeyboardButton(Enum):
	"""Button texts for ReplyKeyboard"""
	SMART_SELECTION_BTN = '🎬Smart Selection'
	WE_RECOMMEND_BTN = '🎯We recommend'
	NO_PREFERENCES_BTN = '👀No preferences'
	SEND_FEEDBACK_BTN = '🎭Send feedback'

class CustomInlineKeyboardButton(Enum):
	"""Button texts for InlineKeyboard"""
	DEPRESSION_BTN = '🌧Depressed'
	CHEERFUL_BTN = '💃Сheerful'
	DONT_KNOW_BTN = "🎲Don't know"
	LOT_ON_MY_MIND_BTN = '🕳Many thoughts'
	STRESSED_OUT_BTN = '💣Stressed out'
	NO_STRENGTH_AT_ALL_BTN = '😮‍💨No energy'
	FIGHTING_SPIRIT_BTN = '😼Fighting mood'
	FAMILY_WEEKEND_BTN = '👨‍👩‍👧‍👦Family'
	GROUP_OF_FRIENDS_BTN = '🍻Friends'
	LOVE_BTN = '💋Love'
