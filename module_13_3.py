from aiogram import Bot, dispatcher, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Бот напечатал в телеге: "Привет! Я бот, помогающий твоему здоровью."')
    await message.answer('Привет! Я бот, помогающий твоему здоровью')

@dp.message_handler()
async def all_messages(message):
    print('Бот напечатал в телеге: "Введите команду /start, чтобы начать общение."')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


