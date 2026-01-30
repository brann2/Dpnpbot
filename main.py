import discord
import random
from config import TOKEN

WELCOME_CHANNEL_ID = 1417152242817044550
GOODBYE_CHANNEL_ID = 1417152314476859422
BOOST_CHANNEL_ID = 1417152381291860118
BOOSTER_ROLE_ID = 1437740399786459247    
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

    # ================= Booster =================
    async def on_member_update(self, before, after):
        # Seseorang baru saja boost
        if before.premium_since is None and after.premium_since is not None:
            channel = after.guild.get_channel(BOOST_CHANNEL_ID)

            if channel:
                embed = discord.Embed(
                    title="🚀 SERVER BOOST!",
                    description=f"Terima kasih {after.mention} sudah boost **{after.guild.name}**! 💜",
                    color=discord.Color.purple()
                )
                embed.add_field(name="Total Boost Server", value=after.guild.premium_subscription_count)
                embed.set_thumbnail(url=after.display_avatar.url)

                await channel.send(embed=embed)

            # 🎁 Kasih role Booster
            role = after.guild.get_role(BOOSTER_ROLE_ID)
            if role:
                try:
                    await after.add_roles(role)
                except discord.Forbidden:
                    print("Tidak punya izin kasih role booster")

            # 💌 Kirim DM ke booster
            try:
                await after.send(f"Terima kasih sudah boost {after.guild.name}! Kamu dapat role spesial 💜")
            except:
                pass

        # Server naik level boost
        if before.guild.premium_tier < after.guild.premium_tier:
            channel = after.guild.get_channel(BOOST_CHANNEL_ID)
            if channel:
                await channel.send(
                    f"@everyone 🎉 Server naik ke **LEVEL {after.guild.premium_tier}** berkat para booster! Terima kasih 💜"
                )
    

    # ================= COMMAND =================
    async def on_message(self, message):
        if message.author == self.user:
            return

        msg = message.content.lower()

        if msg.startswith('!halo'):
            await message.channel.send('Halo juga! 👋')
        
        if msg.startswith('!pagi'):
            await message.channel.send('morning jga udh sarapan blm')
        
        if msg.startswith('!turu'):
            await message.channel.send('tidur ya jaga kesehatan mu')

        elif msg.startswith('!ping'):
            await message.channel.send('Pong! 🏓')

        elif msg.startswith('!among'):
            await message.channel.send('@everyone  Ayo Among Us!')
        
        elif msg.startswith('!Among'):
            await message.channel.send('@everyone  Ayo Among Us!')

        elif msg.startswith('!roblox'):
            await message.channel.send('@everyone  Langsung aja Roblox!')

        elif msg.startswith('!Roblox'):
            await message.channel.send('@everyone  Langsung aja Roblox!')
        
        elif msg.startswith('!yuka'):
            await message.channel.send('hallo kak cantik gmn kabarnya')
        
        elif msg.startswith('!ryan'):
            await message.channel.send('Hallo Ganteng')
        
        elif msg.startswith('!kiwi'):
            await message.channel.send('Apeeeeeeeeee')
        
        elif msg.startswith('!ml'):
            await message.channel.send('@everyone  Langsung aja ml yg mau ikut!')

        elif msg.startswith('!gg'):
            await message.channel.send('infokan mancing fish it')

        elif msg.startswith('!brann'):
            await message.channel.send('Hallo owner baik dan ganteng')
        
        elif msg.startswith('!king'):
            await message.channel.send('Gais Kalian Baik Baik aja gwencana ya')

        elif msg.startswith('!maul'):
            await message.channel.send('maul berak celana di sekolah')
        
        elif msg.startswith('!yeay'):
            await message.channel.send('adik terbaik sedipienpi ')

        elif msg.startswith('!wann'):
            await message.channel.send('wann Login ada yang mau minta gendong tuh')

        elif msg.startswith('!itik'):
            await message.channel.send('info roblox/ml  brannn')

        elif msg.startswith('!putra'):
            await message.channel.send('ytta')

        elif msg.startswith('!diyana'):
            await message.channel.send('Apakabar anak anak absen dlu satu satu')
        
        elif msg.startswith('!bii'):
            await message.channel.send('Hallo my Kisah 📖')
                    

        
        elif msg.startswith('!kiss'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media1.tenor.com/m/1fNT0SY5cjwAAAAd/nene-nene-amano.gif",
                    "https://media1.tenor.com/m/Fvwt33eN3hUAAAAC/anime-cute.gif"
                    "https://media1.tenor.com/m/iDQT9BjSSXsAAAAC/kimsoohyun-kimjiwon.gif"
                ])
                embed = discord.Embed(
                    description=f"{message.author.mention} mencium {target.mention} 😘",
                    color=discord.Color.pink()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!slap'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media1.tenor.com/m/bO1H2Zv_5doAAAAC/mai-mai-san.gif",
                    "https://media1.tenor.com/m/WYmal-WAnksAAAAd/yuzuki-mizusaka-nonoka-komiya.gif"
                ])
                embed = discord.Embed(
                    description=f"{message.author.mention} menampar {target.mention} 🖐️",
                    color=discord.Color.red()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!hug'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://media1.tenor.com/m/G_IvONY8EFgAAAAC/aharen-san-anime-hug.gif"
                embed = discord.Embed(
                    description=f"{message.author.mention} memeluk {target.mention} 🤗",
                    color=discord.Color.green()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!bite'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://c.tenor.com/8YpRZ4H7dWkAAAAC/anime-bite.gif"
                embed = discord.Embed(
                    description=f"{message.author.mention} menggigit {target.mention} 😈",
                    color=discord.Color.orange()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!pat'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://c.tenor.com/LUqLUEvFZ8kAAAAC/anime-head-pat.gif"
                embed = discord.Embed(
                    description=f"{message.author.mention} menepuk kepala {target.mention} 🥰",
                    color=discord.Color.blurple()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!kill'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media.tenor.com/HqHu-BqxJUEAAAAi/anime-xd.gif",
                    "https://media1.tenor.com/m/230mTazmYVYAAAAC/anime-anime-boy.gif"
                ])
                embed = discord.Embed(
                    description=f"{message.author.mention} menyerang {target.mention} ⚔️",
                    color=discord.Color.dark_red()
                )
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
client.run(TOKEN)
