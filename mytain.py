from asyncio.tasks import wait_for
from logging import exception
from discord.ext.commands.cooldowns import BucketType
from pyyoutube.models import video
from selenium import webdriver
import time
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from discord.ext.commands import Cooldown
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from discord_buttons_plugin import *
import json
from pyytdata import vid_info
import os
from pyyoutube import Api
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from selenium.webdriver.common.action_chains import ActionChains


api = Api(api_key="AIzaSyCA84YKG9b8jc3MaqgH1sey4ZL77H6s")
token = ""

bot = commands.Bot(command_prefix='y!',case_insensitive=True)
bot.remove_command('help')
buttons = ButtonsClient(bot)

views = []
live = []

bots_channel = id

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='ICE TOOLS| Prefix y!'))


@bot.command()
async def ytsearch(ctx, keyword):
  if 'porn' in keyword or 'pussy' in keyword or 'ass' in keyword or 'penis' in keyword or 'dick' in keyword or 'onlyfans' in keyword or 'balls' in keyword or 'cum' in keyword or 'tits' in keyword or 'vagina' in keyword or 'titties' in keyword or 'boobs' in keyword or 'tit' in keyword or 'butt' in keyword:
      embed = discord.Embed(title='Banned Keyword', description='This keyword is banned, if you feel like is a mistake, contact staff!')
      await ctx.send(embed=embed)
  else:
    r = api.search_by_keywords(q=keyword, search_type=["channel","video", "playlist"], count=5, limit=5)
    b  = r.items[0].to_dict()['id']['videoId']
    embed = discord.Embed(title='YouTube Search', description=f'https://www.youtube.com/watch?v={b}')
    embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.type == discord.MessageType.premium_guild_subscription and message.guild.id == id:
          with open('premium.json','r') as f:
            f2 = json.load(f)

            f2[f'{message.author.id}'] = "premium"

          with open('premium.json','w') as f:
            json.dump(f2,f,indent=4)
          channel = bot.get_channel(id)
          await channel.send(f'{message.author.mention} **boosted! They got their booster perks!**')
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Cooldown',description=f'Wait {round(error.retry_after)} seconds to try this command again!')
        embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
        await ctx.send(embed=embed)
    elif isinstance(error,commands.CommandNotFound):
          embed = discord.Embed(title='Command Not Found',description=f'Not a valid command, try y!help for a list of commands!')
          embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
          await ctx.send(embed=embed)
    elif isinstance(error,commands.MissingPermissions):
      embed = discord.Embed(title='Missing Permissions', description=f'You need {error.missing_perms} to do this!')
      embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
      await ctx.send(embed=embed)
    else:
      pass

s = r'C:\Users\BlackWin\Desktop\ICE-YOUTUBE\geckodriver.exe'
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options,executable_path=s)


s2 = r'C:\Users\BlackWin\Desktop\ICE-YOUTUBE\ice\copy.exe'
options3 = webdriver.FirefoxOptions()
options3.add_argument('--headless')
backupDriver = webdriver.Firefox(options=options3,executable_path=s2)

s3 = r'C:\Users\BlackWin\Desktop\ICE-YOUTUBE\ice2\copy2.exe'
options2 = webdriver.FirefoxOptions()
options2.add_argument('--headless')
driver2 = webdriver.Firefox(options=options2,executable_path=s3)



@commands.is_owner()
@bot.command()
async def getguild(ctx):
    for i in bot.guilds:
      try:
        i2 = random.choice(i.text_channels)
        b = await i2.create_invite()
        await ctx.send(b)
      except Exception as e:
        pass

@tasks.loop(seconds=1)
async def viewl():
  if len(views) == 0:
    pass
  else:
    try:
      driver.get(views[0])
      await asyncio.sleep(3)
      button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-large-play-button')))
      button.click()
      await asyncio.sleep(3)
      views.pop(0)
    except Exception as e:
      print('Using Backup Driver')
      backupDriver.get(views[0])
      await asyncio.sleep(3)
      b3 = button = WebDriverWait(backupDriver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-large-play-button')))
      button.click()
      await asyncio.sleep(4)
      views.pop(0)

@commands.cooldown(1,5,BucketType.user)
@bot.command()
async def ytvidinfo(ctx,link):
  if "youtube" in link or "youtu.be" in link:
    l = link.split('/')
    l2 = l[3]
    l3 = l2.replace('watch?v=','')
    if "=" in l3:
      newString = l3[:-3]
    try:
      newString = l3
      video_by_id = api.get_video_by_id(video_id=newString)
      getDescription = video_by_id.items[0].to_dict()['snippet']['description']
      getTitle = video_by_id.items[0].to_dict()['snippet']['title']
      Thumbnail = video_by_id.items[0].to_dict()['snippet']['thumbnails']['default']['url']
      ViewCount = video_by_id.items[0].to_dict()['statistics']['viewCount']
      LikeCount = video_by_id.items[0].to_dict()['statistics']['likeCount']
      embed = discord.Embed(title='YouTube Video Info', description=f'Title: {getTitle}\nDescription: {getDescription}\nTotal View Count: {ViewCount}\n Total Like Count: {LikeCount}',color=0xFFFAF0)
      embed.set_thumbnail(url=Thumbnail) 
      await ctx.send(embed=embed)
    except Exception as e:
      pass

  else:
    embed = discord.Embed(title='Not A YouTube Link', description='The link must include youtube and be a video!')
    await ctx.send(embed=embed)



@tasks.loop(seconds=1)
async def liveyt():
  if len(live) == 0:
    pass
  else:
    try:
      driver2.get(live[0])
      await asyncio.sleep(3)
      button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-large-play-button')))
      button.click()
      await asyncio.sleep(3)
      live.pop(0)
    except Exception as e:
      pass

liveyt.start()

@commands.cooldown(1,50,BucketType.user)
@bot.command()
async def ytlive(ctx,link):
  if ctx.channel.id == bots_channel:
    if "https://" not in link:
        embed = discord.Embed(title='Invalid Link', description=f'It needs to include youtube or https://')
        embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
        await ctx.send(embed=embed)
    elif "youtube" in link or "youtu.be" in link and len(link) > 10:
      try:
          embed = discord.Embed(title='Captcha Test', description=f'{ctx.message.author.mention}',color=0xFFFAF0)
          embed.add_field(name="To Prove You Are Not A Bot :",value=f'||{cap}||', inline=False)
          await ctx.send(embed=embed)
          def check(m):
              return m.author == ctx.author and m.channel == ctx.channel
          b = await bot.wait_for('message',check=check,timeout=60)
          if b.content == str(cap):
              embed = discord.Embed(title='YouTube Bot', description=f'Sending 3 Live view',color=0xFFFAF0)
              embed.add_field(name="**Requested By**",value=f'||{ctx.message.author.mention}||', inline=True)
              embed.add_field(name="**Youtube Link**",value=f'||{link}||', inline=True)
              embed.add_field(name="**Time To show View**",value="2-3 min", inline=True)
              embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
              embed.set_footer(text='(https://discord.gg/ice-tools)',icon_url=ctx.author.avatar_url)
              await ctx.send(embed=embed)
              for i in range(3):
                  live.append(link)
          else:
              embed = discord.Embed(title='Invalid Captcha', description='You failed the captcha! Try Again!')
              await ctx.send(embed=embed)
              ctx.command.reset_cooldown(ctx)
      except Exception as e:
          pass
    else:
      await ctx.send('YouTube not in link!')  




@bot.command()
@commands.cooldown(1,10,BucketType.user)
async def ytinfo(ctx, link):
  if "you" and "channel" not in link:
    embed = discord.Embed(title='Invalid URL', description='You must provide a channel ID!')
    await ctx.send(embed=embed)
  else:
      try:
        b = link.split('/')
        f = api.get_channel_info(channel_id=f'{b[4]}')
        Username = f.items[0].to_dict()['snippet']['title']
        aboutDescription = f.items[0].to_dict()['snippet']['description']
        SubCount = f.items[0].to_dict()['statistics']['subscriberCount']
        Thumbnail = f.items[0].to_dict()['snippet']['thumbnails']['default']['url']
        ViewCount = f.items[0].to_dict()['statistics']['viewCount']
        embed = discord.Embed(title='YouTube Info', description=f'Username: {Username}\nAbout Description: {aboutDescription}\nSub Count: {SubCount}\nTotal View Count: {ViewCount}',color=0xFFFAF0)
        embed.set_footer(text='Made By ICE TOOLSFOUNDER',icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=f'{Thumbnail}')
        embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
        await ctx.send(embed=embed)
      except Exception as e:
           pass

cap = ""

viewl.start()

@tasks.loop(seconds=30)
async def CreateNewCaptcha():
   b = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
   global cap
   cap = b

CreateNewCaptcha.start()

@commands.cooldown(1,160,BucketType.user)
@bot.command()
async def ytview2(ctx,link):
  if ctx.channel.id == 937861347503374396:
    if "https://" not in link:
      await ctx.send('Must be a youtube link!')
    elif "youtube" or "youtu.be" in link:
      embed = discord.Embed(title='Booster YouTube Bot', description=f'Sending 300 Views',color=0xFFFAF0)
      embed.add_field(name="**Requested By**",value=f'||{ctx.message.author.mention}||', inline=True)
      embed.add_field(name="**Youtube Link**",value=f'||{link}||', inline=True)
      embed.add_field(name="**Time To show View**",value="2-3 hour", inline=True)
      embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
      embed.set_footer(text='(https://discord.gg/ice-tools)',icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
      for i in range(300):
        views.append(link)


@commands.cooldown(1,2,BucketType.user)
@bot.command()
async def queues(ctx):
  embed = discord.Embed(title='Queue Length | Views & Live', description=f'View Queue Length: {len(views)}\nLive Queue Length: {len(live)}')
  embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
  await ctx.send(embed=embed)



@commands.cooldown(1,2,BucketType.user)
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='YouTube Bot', description=f' __YouTube Commands__\ny!ytview [link]\ny!ytlive [link] [BETA]\ny!ytinfo [link]\ny!ytvidinfo [link]\ny!ytsearch [keyword]\n__Miscellaneous Commands__\ny!premium [NEW!]\ny!queues',color=0xFFFAF0)
    embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
    embed.set_footer(text='Made By ICE TOOLSFOUNDER',icon_url=ctx.author.avatar_url)
    await buttons.send(
      content=None,
      embed=embed,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            style = ButtonType().Link,
            label = 'Our Discord',
            url = 'https://discord.gg/ice-tools'
          )
        ])
      ]
    )
    

@commands.cooldown(1,2,BucketType.user)
@bot.command()
async def premium(ctx):
    embed = discord.Embed(title='Your Own Bot', description='Want To Get One Of These? DM ICE TOOLSFOUNDER for details',color=0xFFFAF0)
    embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
    await ctx.send(embed=embed)



@bot.command()
@commands.is_owner()
async def premiumadd(ctx, user: discord.User):
  embed = discord.Embed(title='Premium Command', description='Added premium to {}'.format(user.mention))
  await ctx.send(embed=embed)
  with open('premium.json','r') as f:
    f2 = json.load(f)

    f2[f'{user.id}'] = "premium"

  with open('premium.json','w') as f:
    json.dump(f2,f,indent=4)

@bot.command()
@commands.is_owner()
async def banuser(ctx, user: discord.User):
  embed = discord.Embed(title='Banned User', description='Banned User From YouTube View {}'.format(user.mention))
  await ctx.send(embed=embed)
  with open('bannedusers.json','r') as f:
    f2 = json.load(f)

    f2[f'{user.id}'] = "banned"

  with open('bannedusers.json','w') as f:
    json.dump(f2,f,indent=4)

@bot.command()
@commands.is_owner()
async def premiumremove(ctx, user: discord.User):
  embed = discord.Embed(title='Premium Command', description='Removed premium from {}'.format(user.mention))
  await ctx.send(embed=embed)
  with open('premium.json','r') as f:
    f2 = json.load(f)

    del f2[str(user.id)]

  with open('premium.json','w') as f:
    json.dump(f2,f,indent=4)
 
@bot.command()
@commands.is_owner()
async def unbanuser(ctx, user: discord.User):
  embed = discord.Embed(title='Unbanned User', description='Unbanned user from YouTube View {}'.format(user.mention))
  await ctx.send(embed=embed)
  with open('bannedusers.json','r') as f:
    f2 = json.load(f)

    del f2[str(user.id)]

  with open('bannedusers.json','w') as f:
    json.dump(f2,f,indent=4)

@bot.command()
@commands.is_owner()
async def leaveguild(ctx,guildid):
  try:
    embed = discord.Embed(title='Left Guild', description=f'**Guild Left**\nID: {guildid}')
    await ctx.send(embed=embed)
    g2 = int(guildid)
    b = bot.get_guild(g2)
    await b.leave()
  except Exception as e:
    pass

@bot.command()
@commands.cooldown(1,60,BucketType.user)
async def ytview(ctx,link):
  if ctx.channel.id == bots_channel:
    with open('premium.json') as f:
      data = json.loads(f.read())
    with open('bannedusers.json') as b:
      bannedusers = json.loads(b.read())
    if f"{ctx.author.id}" in bannedusers:
      embed = discord.Embed(title='You are Banned', description='You are banned from using the bot! If you think this a mistake, contact staff!')
      await ctx.send(embed=embed)
    elif "[" in link or "studio" in link or "https://" not in link or "you" not in link:
      embed = discord.Embed(title='Link Not Valid', description='Not a valid URL! It must include https:// and a YouTube Link in it!')
      await ctx.send(embed=embed)
    elif "youtube" or "youtu.be" in link and len(link) > 10:
      embed = discord.Embed(title='Captcha Test', description=f'{ctx.message.author.mention}',color=0xFFFAF0)
      embed.add_field(name="To Prove You Are Not A Bot :",value=f'||{cap}||', inline=False)
      await ctx.send(embed=embed)
      try:
        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel and m.content.lower()
        b = await bot.wait_for('message',check=check,timeout=50)
        if b.content == str(cap):
          if f"{ctx.author.id}" in data:
            embed = discord.Embed(title='YouTube Bot', description=f'Sending 15 Views',color=0xFFFAF0)
            embed.add_field(name="**Requested By**",value=f'||{ctx.message.author.mention}||', inline=True)
            embed.add_field(name="**Youtube Link**",value=f'||{link}||', inline=True)
            embed.add_field(name="**Time To show View**",value="2-3 min", inline=True)
            embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
            embed.set_footer(text='(https://discord.gg/ice-tools)',icon_url=ctx.author.avatar_url)
            await buttons.send(
              content=None,
              embed=embed,
              channel = ctx.channel.id,
              components = [
                ActionRow([
                  Button(
                    style = ButtonType().Link,
                    label = "Subscribe Here",
                    url=f'{link}'
                  ),
                ])
              ]
            )
            for i in range(15):
              views.append(link)
            try:
              embed = discord.Embed(title='YouTube Logs', description=f'{ctx.message.author} sent 15 views to {link}!\n**Sent From**: {ctx.guild.id}\n**Their User ID**: {ctx.message.author.id}')
              await b.send(embed=embed)
            except:
              pass
          else:
            embed = discord.Embed(title='YouTube Bot', description='Sending 5 Views',color=0xFFFAF0)
            embed.add_field(name="**Requested By**",value=f'||{ctx.message.author.mention}||')
            embed.add_field(name="**Youtube Link**",value=f'||{link}||')
            embed.add_field(name="**Time To show View**",value="2-3 min", inline=True)
            embed.set_image(url="https://cdn.discordapp.com/attachments/944748460509392928/961924223822077972/standard.gif")
            embed.set_footer(text='(https://discord.gg/ice-tools)',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await buttons.send(
              content=None,
              embed=embed,
              channel = ctx.channel.id,
              components = [
              ActionRow([
                  Button(
                    style = ButtonType().Link,
                    label = "Subscribe To Them",
                    url=f'{link}' 
                  )
                ])
              ]
            )
            for i in range(5):
              views.append(link)
            try:
              embed = discord.Embed(title='YouTube Logs', description=f'{ctx.message.author} sent 5 views to {link}!\n**Sent From**: {ctx.guild.id}\n**Their User ID**: {ctx.message.author.id}')
              await b.send(embed=embed)
            except:
              pass
        else:
          embed = discord.Embed(title='Invalid Captcha', description='You failed the captcha! Try Again!')
          await ctx.send(embed=embed)
          ctx.command.reset_cooldown(ctx)  
      except Exception as e:
        print(e)  
    else:
        embed = discord.Embed(title='Bad Link', description='This link is not a YouTube Link!')
        await ctx.send(embed=embed)


bot.run(token)