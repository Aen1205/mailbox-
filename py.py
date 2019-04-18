import discord
import os 

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='매일 받는중..', type=1))


@client.event
async def on_message(message):
   if message.channel.is_private and message.author.id != "568435595429412865":
      await client.send_message(discord.utils.get(client.get_all_mambers(), id="504559604412448768"), message.author.name + "(" + message.author.id + ") : " + messag.content)

if message.channel.is_private and message.author.id != "568435595429412865":
      await client.send_message(client.get_channel("568437836785778719"), id="504559604412448768"), message.author.name + "(" + message.author.id + ") : " + messag.content)

if message.content.startswith("SD")
    member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
    await client.send_message(member, "앤이 보낸 편지 : " + message.content[23:])

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
