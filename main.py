from aiogram import executor
from loader import dp
import handlers


async def on_startup(dispatcher):
    await set_default_command(dispatcher)

    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)