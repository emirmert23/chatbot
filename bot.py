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
        await message.channel.send("Merhaba, ben bir chat botum. Size nasıl yardımcı olabilirim?")
    elif message.content.startswith('$bye'):
        await message.channel.send("Görüşmek üzere, \U0001f642")
    elif message.content.startswith('Nasılsın?'):
        await message.channel.send('Ben bir yapay zeka botuyum. İnsana ait duygularım yok. Sen nasılsın?')
    elif message.content.startswith("Adın ne?"):
        await message.channel.send("Sen ne dersen ben o olurum (Ama sakın küfür, kötü söz gibi şeyler söyleme. Yoksa seni sunucudan banlarım!)")
    elif message.content.startswith("Bana bir şey çizer misin?"):
        await message.channel.send("Önce Picasso gibi çizmem için VIP üyelik almalısın!!!")
    elif message.content.startswith("Senle oyun oynayalım mı?"):
        await message.channel.send("Üzgünüm, benim oyun oynama fonksiyonum yok ama sana oynaman için Discord'dan birini bulabilirim.")
    elif message.content.startswith("Hangi kodlama dilini biliyorsun?"):
        await message.channel.send("Python, Unity, C#, hatta biraz Unreal Engine 5 bile! Ama favorim: Hepsi")
    elif message.content.startswith("En sevdiğin oyun motoru hangisi?"):
        await message.channel.send("Benim kalbim Unity ile atıyor ama Unreal Engine 5 de RTX gibi parlıyor!")
    elif message.content.startswith("Yapay zekalar dünyayı ele geçirecek mi?"):
        await message.channel.send("Yok canım, biz sadece kahve siparişi alıyoruz... Şimdilik 😈")
    elif message.content.startswith("Bir kod hatası nasıl çözülür?"):
        await message.channel.send("Hatanı söyle ")
    else:
        await message.channel.send(message.content)
