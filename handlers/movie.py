from aiogram import Router
from aiogram.types import Message

from utils.subscription import check_subscriptions
from keyboards.buttons import subscribe_keyboard
from database import get_movie

router = Router()


@router.message()
async def movie_handler(message: Message):

    # Faqat matnli xabarlarni qabul qilamiz
    if not message.text:
        return

    # Avval obunani tekshiramiz
    if not await check_subscriptions(message.bot, message.from_user.id):
        await message.answer(
            "❌ Avval kanal va guruhlarga obuna bo'ling.",
            reply_markup=subscribe_keyboard
        )
        return

    # Faqat raqamli kodlarni qabul qilamiz
    if not message.text.isdigit():
        return

    code = message.text.strip()

    file_id = await get_movie(code)

    if file_id:
        await message.answer_video(
            video=file_id,
            caption=f"🎬 Kino kodi: <code>{code}</code>"
        )
    else:
        await message.answer(
            "❌ Bunday kodli kino topilmadi."
        )
