from aiogram import Bot, Dispatcher, exceptions
from settings import settings
import asyncio
from handlers import router


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    except exceptions.TelegramNetworkError:
        await restart_bot(bot, dp)
    except KeyboardInterrupt:
        print('Exit')


async def restart_bot(bot: Bot, dp: Dispatcher):
    await bot.session.close()
    await asyncio.sleep(1)
    try:
        await dp.start_polling(bot)
    except exceptions.TelegramNetworkError:
        await restart_bot(bot, dp)


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Exit')
