from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 1-kanal",
                url="https://t.me/pro_kinolar_n1"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 2-kanal",
                url="https://t.me/clash_akk_savdo"
            )
        ],
        [
            InlineKeyboardButton(
                text="👥 Guruh",
                url="https://t.me/clash_of_clans_akaunt_savdo_chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Obunani tekshirish",
                callback_data="check_sub"
            )
        ]
    ]
)

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Kino qo'shish",
                callback_data="add_movie"
            )
        ],
        [
            InlineKeyboardButton(
                text="📊 Statistika",
                callback_data="statistics"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Reklama yuborish",
                callback_data="broadcast"
            )
        ]
    ]
)
