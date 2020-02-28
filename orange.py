import os
import aiohttp

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name= 'fib')
async def fibonacci(ctx, x: int):
    sign = -1 if x < 0 else 1
    a, b = 0, sign*1
    fib = []
    for _ in range(abs(x)):
        fib.append(a)
        a, b = b, b + a
    await ctx.send(str(fib)[1:-1])

bot.run(token) 
