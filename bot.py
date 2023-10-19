import discord
from modelka import detect_tree

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        for i in message.attachments:
            file_name = i.filename
            await i.save(f'./image/{file_name}') 
            classs, tohnost = detect_tree(f'./image/{file_name}', 'keras_model.h5', 'labels.txt')
            if tohnost > 0.6:
                await message.channel.send(f'класс-{classs} точность-{tohnost}')
            else:
                await message.channel.send(f'сам думай что это, я не знаю')
                

client.run('')
