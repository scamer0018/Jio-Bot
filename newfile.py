import sys
sys.stdout.reconfigure(encoding='utf-8')

print("বাংলা লেখা ঠিকমতো দেখাচ্ছে!")
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔹 আপনার BotFather থেকে পাওয়া API টোকেন এখানে বসান
API_TOKEN = "7926863210:AAFG7dTXJDrkWGIAlKvuAJ4uNpy6BkRtmZw"

# 🔹 বটের সেটআপ
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 🔹 যখন কেউ /start কমান্ড পাঠাবে, তখন বট কী রিপ্লাই দেবে
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Wᴇʟʟᴄᴏᴍᴇ Tᴏ Oᴛᴘ ʙᴏᴛ ғᴏʀ ʀᴇᴀʟ Oᴛᴘ Sɪᴛᴇ Fᴏʀ Tᴇʟᴇɢʀᴀᴍ")

# 🔹 যখন কেউ মেসেজ পাঠাবে, তখন বট সেটার রিপ্লাই দেবে
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

# 🔹 বট চালু করা
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    python bot.py