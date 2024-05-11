token = "MTIzNjU4MTI3MDI4OTM4MzQ5NQ.GDVbpb.JzT7tdZ5VSR9CP2ezRSr9GRtFYghWvNHsNXx44"
import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('halo'):
        await message.channel.send("kenapa woi")
    elif message.content.startswith('udah dulu ya'):
        await message.channel.send("yakin mau pergi?")
    else:
        await message.channel.send(message.content)

client.run("MTIzNjU4MTI3MDI4OTM4MzQ5NQ.GDVbpb.JzT7tdZ5VSR9CP2ezRSr9GRtFYghWvNHsNXx44")
