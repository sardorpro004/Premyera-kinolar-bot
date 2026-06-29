from aiogram.exceptions import TelegramBadRequest

CHANNELS = [
    "@pro_kinolar_n1",
    "@clash_akk_savdo",
    "@clash_of_clans_akaunt_savdo_chat"
]

async def check_subscriptions(bot, user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except TelegramBadRequest:
            return False
    return True
