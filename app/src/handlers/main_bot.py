from aiogram import types
from aiogram.filters.command import Command

from loader import dp, predictor


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text="Start")
    await message.delete()


@dp.message()
async def any_message(message: types.Message):
    rating = int(predictor.predict(message.text)[0])
    print(f"Get message: {message.text}")
    print(f"Result predictor: {rating}")
    await message.answer(text=f"Ваша оценка: {rating}")
