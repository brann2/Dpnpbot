import discord
from config import TOKEN

WELCOME_CHANNEL_ID = 1417152242817044550
GOODBYE_CHANNEL_ID = 1417152314476859422
AUTO_ROLE_ID = 1438899323336130802

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # ================= WELCOME =================
    async def on_member_join(self, member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)

        if channel:
            embed = discord.Embed(
                title="🎉 WELCOME!",
                description=f"Halo {member.mention}, selamat datang di **{member.guild.name}**!",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_image(url="https://i.imgur.com/OfeFMXC.png")

            await channel.send(embed=embed)

        role = member.guild.get_role(AUTO_ROLE_ID)
        if role:
            try:
                await member.add_roles(role)
            except discord.Forbidden:
                print("Tidak punya izin kasih role")

        try:
            await member.send(f"Hai {member.name}, selamat datang di {member.guild.name}! 🎊")
        except:
            pass

    # ================= GOODBYE =================
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(GOODBYE_CHANNEL_ID)

        if channel:
            embed = discord.Embed(
                title="👋 GOODBYE!",
                description=f"{member.name} telah keluar dari **{member.guild.name}**.\nSemoga kita ketemu lagi ya!",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_image(url="https://i.imgur.com/k3II9KX.jpeg")

            await channel.send(embed=embed)

    # ================= COMMAND =================
    async def on_message(self, message):
        if message.author == self.user:
            return

        msg = message.content.lower()

        if msg.startswith('halo'):
            await message.channel.send('Halo juga! 👋')
        
        if msg.startswith('pagi'):
            await message.channel.send('morning jga udh sarapan blm')
        
        if msg.startswith('turu'):
            await message.channel.send('tidur ya jaga kesehatan mu')

        elif msg.startswith('ping'):
            await message.channel.send('Pong! 🏓')

        elif msg.startswith('among'):
            await message.channel.send('@everyone 🚨 Ayo Among Us!')
        
        elif msg.startswith('Among'):
            await message.channel.send('@everyone 🚨 Ayo Among Us!')

        elif msg.startswith('roblox'):
            await message.channel.send('@everyone 🎮 Langsung aja Roblox!')

        elif msg.startswith('Roblox'):
            await message.channel.send('@everyone 🎮 Langsung aja Roblox!')
        
        elif msg.startswith('yuka'):
            await message.channel.send('hallo kak cantik gmn kabarnya')
        
        elif msg.startswith('ryan'):
            await message.channel.send('suka ngompol di celana')
        
        elif msg.startswith('kiwi'):
            await message.channel.send('gua hancurin isi kepala lu gw gampar lu')
        
        
        elif msg.startswith('ml'):
            await message.channel.send('@everyone 🎮 Langsung aja ml yg mau ikut!')

        elif msg.startswith('gg'):
            await message.channel.send('gg emg suka cowo gaes')

        elif msg.startswith('maul'):
            await message.channel.send('maul berak celana di sekolah')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
client.run(TOKEN)
