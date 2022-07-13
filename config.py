
"""
Contains the config
"""

import os
from dotenv import load_dotenv
from enum import Enum

# get the token from '.env' file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# user's selected mood, show type(movie/series) and genre
# the variables are set in 'callbacks.py' and never changed
USER_MOOD = None
USER_SHOW = None
USER_GENRE = None

# used in 'callbacks.py' for verification
PROCESS_FLAGS = {'mood_selected': False, 'show_selected': False, 'genre_selected': False}

class UserMood(Enum):
	"""
	User's mood variants
	
	using as 'callback_data' in 'keyboards.py', for 'text' in 'callback.py' 
	and as a value for 'USER_MOOD'
	"""
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
	"""Available genres of movies/series which we have in DB"""
	COMEDY = 'comedy'
	THRILLER = 'thriller'
	ACTION = 'action'
	DOCUMENTARY = 'documentary'
	FAMILY = 'family'
	SPORT = 'sport'
	FANTASY = 'fantasy'
	ANIMATION = 'animation'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))

class Show(Enum):
	"""
	What kind of show user wants to watch

	using as 'callback_data' in 'keyboards.py', for 'text' in 'callback.py',
	and as a value for 'USER_SHOW'
	"""
	MOVIE = 'movie'
	SERIES = 'series'

	@classmethod
	def list(cls):
		"""Get a list of values"""
		return list(map(lambda c: c.value, cls))

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
	"""Button texts for InlineKeyboard to process user's mood selection"""
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

	"""Button texts for InlineKeyboard to process user's show selection"""
	MOVIE_BTN = '🎬Movie'
	SERIES_BTN = '🎬🎬Series'

	"""Button texts for InlineKeyboard to process user's genre selection"""
	COMEDY_BTN = '🕺Comedy'
	THRILLER_BTN = '🔫Thriller'
	ACTION_BTN = '🎒Action'
	DOCUMENTARY_BTN = '🎥Documentary'
	FAMILY_BTN = '👨‍👩‍👦Family'
	SPORT_BTN = '🚴‍♀️Sport'
	FANTASY_BTN = '🔮Fantasy'
	ANIMATION_BTN = '🧸Animation'
