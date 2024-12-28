import asyncio
from aiogram import F,Bot, Dispatcher, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.filters import CommandStart, Command

#from config import token
TOKEN = "5931999116:AAGkxO8594HDwRVyjcuV5hA-9_nAQJSGng0"

# Основная асинхронная функция
async def main():
    try:
        bot = Bot(token=TOKEN)
        dp = Dispatcher()
        print("Старт...")
        
        reply_start = ReplyKeyboardMarkup(keyboard =[
            [KeyboardButton(text='Меню')],
            [KeyboardButton(text='Поддержка'), KeyboardButton(text='Поиск')],
            [KeyboardButton(text ='Назад')]
          ], resize_keyboard =True)
        
        router = Router()
        @router.message(CommandStart())
        async def cmd_start(message: Message):
            await message.answer("Привет! Я бот, готов помочь вам. Используйте команду /help, чтобы узнать, что я умею.", reply_markup =reply_start)
        
        @router.message(Command('about'))
        async def cmd_about(message: Message ):
            await message.answer("Вы вызвали команду about")
        call_router =Router()
        @call_router.message(F.text == 'Меню')
        async def menu(message: Message):
            await message.answer('Вы нажали меню')
          # Tab to edit
          # Tab to edit 
        dp.include_router(router)
        dp.include_router(call_router)
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
await main()