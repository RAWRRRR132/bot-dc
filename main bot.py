import os
import discord # type: ignore
from discord.ext import commands # type: ignore
from botlogic import pass_gen

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command
async def passgen(ctx):
    await ctx.send('halo berikut password kamu')
    await ctx.send(pass_gen())

@bot.command()
async def pangkatdua(ctx):
    await ctx.send('masukan angka bebas,nanti aku hitumg pankat 2 nya')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f"pangkat dua dari angka yang kamu kirimkan adalah {new_varin(message.content)**2}") # type: ignore
@bot.command()
async def meme(ctx):
    import random,os
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file= picture) # type: ignore

daur_ulang= ['sampah kaca','plastik','kertas',
            'logam','tekstil','barang elektronik']

@bot.command()
async def cek_sampah(ctx):
    await ctx.send('apa sampah yang mau kamu priksa?')
    message = await bot.wait_for('message',check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message= str('message')

    if message.lower in daur_ulang:
        await ctx.send('sampah tersebut harus di daur ulang,berikut tips daur ulang')
        await ctx.send('isi link artikel/vt/youtube dll')
    else:
        await ctx.send('sampah tersebut bisa dimusnahkan atau dibuang dengan bijak')
        await ctx.send('kasih artikel terkait!')
