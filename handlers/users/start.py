from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import *
import logging
import re
from loader import dp, bot



logging.basicConfig(level=logging.INFO)


link_pattern = re.compile(
    r"""(
        https?://\S+ |                    
        t\.me/[\w\d_+/]+ |                
        joinchat/\S+ |                    
        \S+\.(com|net|org|ru|uz|io|xyz|site|store|info|app|online|biz) |
        @[\w\d_]*bot\b                   # Mentions of bots (e.g. @somebot)
    )""",
    re.IGNORECASE | re.VERBOSE
)


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = """Добавьте меня в группу и я буду удалять все рекламы
Meni guruhga qo'shing va men hamma reklamalarni o'chirib tashlayman""")
    await message.delete()
    

@dp.message_handler(lambda message: link_pattern.search(message.text or ""))
async def delete_if_link(message: types.Message):
    try:
        await message.delete()
        logging.info(f"Deleted message from {message.from_user.full_name}")
    except Exception as e:
        logging.warning(f"Could not delete message: {e}")