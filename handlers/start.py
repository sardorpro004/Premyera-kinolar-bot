from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.buttons import subscribe_keyboard
from utils.subscription import check_subscriptions

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    if await check_subscriptions(message.bot, message.from_user.id):
        await message.answer(
            "✅ Obunangiz tasdiqlandi!\n\n🎬 Endi kino kodini yuboring."
        )
    else:
        await message.answer(
            "❌ Botdan foydalanish uchun quyidagi kanal va guruhga obuna bo'ling.",
            reply_markup=subscribe_keyboard
        )


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    if await check_subscriptions(callback.bot, callback.from_user.id):
        await callback.message.edit_text(
            "✅ Obunangiz tasdiqlandi!\n\n🎬 Endi kino kodini yuboring."
        )
    else:
        await callback.answer(
            "❌ Hali hamma joyga obuna bo'lmagansiz!",
            show_alert=True
        )
