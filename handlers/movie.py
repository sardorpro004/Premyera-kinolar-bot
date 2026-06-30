from aiogram import Router
from aiogram.types import Message

from database import get_movie

router = Router()

@router.message()
async def movie_handler(message: Message):
    code = message.text.strip()

    movie = await get_movie(code)

    if movie:
        await message.answer_video(movie[0])
    else:
        await message.answer("❌ Bunday kodli kino topilmadi.")
