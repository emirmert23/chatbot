import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Merhaba, ben bir chat botum. Size nasıl yardımcı olabilirm")
    elif message.content.startswith('$bye'):
        await message.channel.send("Görüşmek üzere, \U0001f642")
    elif message.content.startswith('Nasılsın?'):
        await message.channel.send('Ben bir yapay zeka botuyum. İnsana ait duygularım yok. Sen nasılsın? ')
    elif message.content.startswith("Adın ne?"):
        await message.channel.send("Sen ne dersen ben o olurum(Ama sakın küfür, kötü söz gibi şeyler söyleme söylersen seni sunucudan banlarım)")
    elif message.content.startswith("Bana bir şey çizer misin?"):
        await message.channel.send("Önce Picasso gibi çizmem için VIP üyelik almalısın!!!")
    elif message.content.startswith("Senle oyun oynayalım mı?"):
        await message.channel.send("Üzgünüm benim oyun oynama fonksiyonum yok ama sana oynaman için Discord'dan birini bulabilirim.")
    elif message.content.startswith("Hangi kodlama dilini biliyorsun?"):
        await message.channel.send("")
    elif message.content.startswith(""):
        await message.channel.send("")
    else:
        await message.channel.send(message.content)
