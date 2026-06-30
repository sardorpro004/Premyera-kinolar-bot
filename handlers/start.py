from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.buttons import subscribe_keyboard
from utils.subscription import check_subscriptions
from database import add_user

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):

    await add_user(message.from_user.id)

    if await check_subscriptions(message.bot, message.from_user.id):
        await message.answer(
            "🎉 Assalomu alaykum!\n\n"
            "✅ Obunangiz tasdiqlandi.\n\n"
            "🎬 Endi kino kodini yuboring."
        )
    else:
        await message.answer(
            "❌ Botdan foydalanish uchun quyidagi kanal va guruhga obuna bo'ling.\n\n"
            "Obuna bo'lgach, pastdagi «✅ Obunani tekshirish» tugmasini bosing.",
            reply_markup=subscribe_keyboard
        )


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):

    if await check_subscriptions(callback.bot, callback.from_user.id):

        await callback.message.edit_text(
            "🎉 Rahmat!\n\n"
            "✅ Obunangiz tasdiqlandi.\n\n"
            "🎬 Endi kino kodini yuboring."
        )

    else:
        await callback.answer(
            "❌ Siz hali barcha kanal va guruhga obuna bo'lmagansiz!",
            show_alert=True
        )
