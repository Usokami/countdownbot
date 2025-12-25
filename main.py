import os
import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TZ = timezone(timedelta(hours=7))
TARGET = datetime(2026, 1, 1, 0, 0, 0, tzinfo=TZ)

@bot.event
async def on_ready():
    print(f"ออนไลน์แล้ว {bot.user}")

@bot.command()
async def ny(ctx):
    msg = await ctx.send("⏳ กำลังตั้งเวลานับถอยหลัง...")

    while True:
        now = datetime.now(TZ)
        diff = TARGET - now
        total = int(diff.total_seconds())

        if total <= 0:
            await msg.edit(
                content="🎆 **HAPPY NEW YEAR 2026!** 🎆"
            )
            break

        sleep_time = 10 if total > 600 else 1

        d = total // 86400
        h = (total % 86400) // 3600
        m = (total % 3600) // 60
        s = total % 60

        await msg.edit(
            content=
            f"⏳ **Countdown ปีใหม่**\n"
            f"🗓 เหลือ {d} day {h:02d} hour {m:02d} min {s:02d} sec"
        )

        await asyncio.sleep(sleep_time)

bot.run(os.getenv("TOKEN"))
