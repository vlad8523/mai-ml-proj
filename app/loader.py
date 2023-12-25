import asyncio
import pickle

import os

from aiogram import Bot, Dispatcher, types

from ML import MovieRatingPrediction

predictor = MovieRatingPrediction()
bot = Bot(token=os.getenv("TOKEN_API"))
dp = Dispatcher()
