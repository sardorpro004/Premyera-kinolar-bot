from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "🎬 Premyera kinolar botiga xush kelibsiz!\n\n"
        "Film olish uchun avval kanallarimizga obuna bo'ling."
    )
