from aiogram import Router
from aiogram.types import Message

from utils.subscription import check_subscriptions
from database import get_movie

router = Router()


@router.message()
async def movie_handler(message: Message):

    # Avval obunani tekshiramiz
    if not await check_subscriptions(message.bot, message.from_user.id):
        await message.answer(
            "❌ Avval kanal va guruhlarga obuna bo'ling.\n/start ni bosing."
        )
        return

    # Faqat raqamli kodlarni qabul qilamiz
    if not message.text or not message.text.isdigit():
        return

    code = message.text.strip()

    movie = await get_movie(code)

    if movie:
        await message.answer_video(
            video=movie[0],
            caption=f"🎬 Kino kodi: {code}"
        )
    else:
        await message.answer(
            "❌ Bunday kodli kino topilmadi."
        )
