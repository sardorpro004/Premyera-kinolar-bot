from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from database import create_db
from config import BOT_TOKEN
from handlers.start import router as start_router
bot = Bot(
    token=BOT_TOKEN,
   from handlers.admin import router as admin_router
    from handlers.movie import router as movie_router
from handlers.movie import router as movie_router
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(start_router)
async def main():
    print("Bot ishga tushdi...")
await create_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
