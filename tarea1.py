import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f'El {bot.user} ha iniciado con exito')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def risa(ctx, count_ja = 5):
    await ctx.send("ja" * count_ja)

@bot.command()
async def adios(ctx):
    await ctx.send(f'Nos vemos!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} se unió {discord.utils.format_dt(member.joined_at)}')

from bot_logic import gen_pass

password = gen_pass(10)
print("Tu nueva contraseña es:", password)

bot.run("TOKEN")
