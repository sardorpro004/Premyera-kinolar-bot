from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import ADMINS
from database import (
    add_movie,
    get_users_count,
    get_all_users
)

router = Router()


class AddMovieState(StatesGroup):
    code = State()
    video = State()


class BroadcastState(StatesGroup):
    message = State()


@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id not in ADMINS:
        return

    users = await get_users_count()

    await message.answer(
        f"""
👨‍💻 <b>ADMIN PANEL</b>

👥 Foydalanuvchilar: <b>{users}</b>

Buyruqlar:

➕ /addmovie - Kino qo'shish

📢 /broadcast - Reklama yuborish
"""
    )


@router.message(Command("addmovie"))
async def add_movie_cmd(message: Message, state: FSMContext):

    if message.from_user.id not in ADMINS:
        return

    await message.answer("🎬 Kino kodini yuboring.")

    await state.set_state(AddMovieState.code)


@router.message(AddMovieState.code)
async def get_code(message: Message, state: FSMContext):

    await state.update_data(code=message.text.strip())

    await message.answer("📹 Endi kinoni video ko'rinishida yuboring.")

    await state.set_state(AddMovieState.video)


@router.message(AddMovieState.video, F.video)
async def save_movie(message: Message, state: FSMContext):

    data = await state.get_data()

    await add_movie(
        data["code"],
        message.video.file_id
    )

    await message.answer(
        f"✅ Kino saqlandi.\n\nKod: <code>{data['code']}</code>"
    )

    await state.clear()


@router.message(Command("broadcast"))
async def broadcast(message: Message, state: FSMContext):

    if message.from_user.id not in ADMINS:
        return

    await message.answer("📢 Reklama matnini yuboring.")

    await state.set_state(BroadcastState.message)


@router.message(BroadcastState.message)
async def send_broadcast(message: Message, state: FSMContext):

    users = await get_all_users()

    success = 0

    failed = 0

    for user in users:

        try:

            await message.copy_to(user[0])

            success += 1

        except:

            failed += 1

    await message.answer(
        f"""
✅ Reklama yakunlandi

✔️ Yuborildi: {success}

❌ Xato: {failed}
"""
    )

    await state.clear()
