import discord
from pylatexenc.latex2text import LatexNodes2Text
import requests
import platform
import os

if platform.uname().node == 'Andrew':
    import config
    discordToken = config.discord_token
else:
    discordToken = os.getenv('discord_token')

intents = discord.Intents(0, messages=True, message_content=True)
client = discord.Client(intents=intents)

#gets link that displays latex as image
def latexRenderURL(latex):
    url = r"https://latex.codecogs.com/png.image?\inline&space;\huge&space;\dpi{120}\bg{white}"
    #replacements to not fuck up url
    replacements = {'(': '\(', ')': '\)', ' ': '&space;'}
    for r in replacements:
        latex = latex.replace(r, replacements[r])
    return url + latex

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #doesn't respond to self
    if message.author == client.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send('Hello!')

    elif 'tex' in message.content.lower() and message.attachments != []:
        #post request to api to get latex
        file = await message.attachments[0].read()
        result = requests.post('http://54.242.209.107/predict/',
                               files={'file': file})

        #make embedded message with result
        embed = discord.Embed(title='Result!', color=0x7CB9E8)
        embed.add_field(name='LaTeX:', value='`' + result.json() + '`', inline=False)

        #text representation of latex
        text = '`' + LatexNodes2Text().latex_to_text(result.json()) + '`'
        embed.add_field(name='Text:', value=text)

        #rendered latex image
        url = latexRenderURL(result.json())
        url.encode('unicode_escape')
        embed.set_image(url=url)
        await message.channel.send(embed=embed)

client.run(discordToken)