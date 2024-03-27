import discord, random
from funct import pass_gen
import discord
from discord.ext import commands
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)
def hitung():
    a = 1
bot = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(f'hi'):
        await message.channel.send(f"Hi!\n\n\n- {client.user}")
    elif message.content.startswith(f'bye'):
        await message.channel.send(f"a\n\n\n- {client.user}")
    elif message.content.startswith(f'flipcoin'):
        await message.channel.send(f'{random.randint(0,1)}\n\n\n- {client.user}')
    elif message.content.startswith(f'pass'):
        await message.channel.send(pass_gen.gen_pass(10))
    @bot.command()
    async def heh(ctx, count_heh = 5):
        await ctx.send("he" * count_heh)

client.run("MTIxODQxNjQyNDQ4NjQzNjkyNQ.GPfLFo.1oN_XwTA_ki1_RuGRgWDpVVgdjVarWm2oZEAr4")