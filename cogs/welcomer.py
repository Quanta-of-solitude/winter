'''
Cog by Quanta#5556
'''
import discord
from discord.ext import commands
import os
import PIL
import myjson
import json
import requests
import shutil
from PIL import Image,ImageFilter,ImageDraw,ImageFont,ImageOps, ImageEnhance
import asyncio


class Welcomer:

    def __init__(self, bot):
        self.bot = bot

    async def have_permissions(ctx):
        return (ctx.author.guild_permissions.administrator == True or ctx.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539)

    def load_url(self):
        '''load the welcome storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["sw_link"] == "link_here":
                storage_link = os.environ.get("sw_link")
            else:
                storage_link = link["sw_link"]
        return storage_link

    def load_url2(self):
        '''load the leave storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["sle_link"] == "link_here":
                storage_link = os.environ.get("sle_link")
            else:
                storage_link = link["sle_link"]
        return storage_link

    def toggle_url(self):
        '''load the welcome storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["toggle_link"] == "link_here":
                storage_link = os.environ.get("toggle_link")
            else:
                storage_link = link["toggle_link"]
        return storage_link

    def toggle_url2(self):
        '''load the leave url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["toggle2_link"] == "link_here":
                storage_link = os.environ.get("toggle2_link")
            else:
                storage_link = link["toggle2_link"]
        return storage_link

    def msg_type(self):
        '''load the type of welcome you need'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["type_link"] == "link_here":
                storage_link = os.environ.get("type_link")
            else:
                storage_link = link["type_link"]
        return storage_link


    @commands.command()
    @commands.check(have_permissions)
    async def welcomemsg(self,ctx, args:str = None, args1:str = None):
        '''set the welcome msg  Syntax w!welcomemsg msg channelid'''
        server = ctx.guild
        url = self.load_url()
        url1 = self.toggle_url()
        if args == None:
            msg = "Welcome! Have fun here <3"
        else:
            msg = args
        if args1 == None:
            channel_id = ctx.channel.id
        else:
            channel_id = args1
        data = myjson.get(url)
        data = json.loads(data)
        data1 = myjson.get(url1)
        data1 = json.loads(data1)
        if "{}".format(server.id) not in data:
            data["{}".format(server.id)] = {}
            data["{}".format(server.id)]["msg"] = "{}".format(msg)
            data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
            data1["{}".format(server.id)] = {}
            data1["{}".format(server.id)]["set_welcome"] = "off"
            url = myjson.store(json.dumps(data),update=url)
            url1 = myjson.store(json.dumps(data1),update=url1)
            em = discord.Embed(description = "Welcome message has been set")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
        else:
            em = discord.Embed(description = "There is a welcome msg (already set), do you want to change it? Reply yes or no")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
            def check(ctx):
                return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')
            msge = await self.bot.wait_for('message', check=check)
            msge.content = msge.content.lower()
            if msge.content == "yes":
                data["{}".format(server.id)] = {}
                data["{}".format(server.id)]["msg"] = "{}".format(msg)
                data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
                data1["{}".format(server.id)] = {}
                data1["{}".format(server.id)]["set_welcome"] = "on"
                url = myjson.store(json.dumps(data),update=url)
                url1 = myjson.store(json.dumps(data1),update=url1)
                em = discord.Embed(description = "Welcome message has been set")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "Edit command Terminated :D")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)


    @commands.command()
    @commands.check(have_permissions)
    async def leavemsg(self,ctx, args:str = None, args1:str = None):
        '''set the leave msg  Syntax w!leavemsg msg channelid'''
        server = ctx.guild
        url = self.load_url2()
        url1 = self.toggle_url2()
        if args == None:
            msg = "Bye, you will be missed :frowning:"
        else:
            msg = args
        if args1 == None:
            channel_id = ctx.channel.id
        else:
            channel_id = args1
        data = myjson.get(url)
        data = json.loads(data)
        data1 = myjson.get(url1)
        data1 = json.loads(data1)
        if "{}".format(server.id) not in data:
            data["{}".format(server.id)] = {}
            data["{}".format(server.id)]["msg"] = "{}".format(msg)
            data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
            data1["{}".format(server.id)] = {}
            data1["{}".format(server.id)]["set_leave"] = "off"
            url = myjson.store(json.dumps(data),update=url)
            url1 = myjson.store(json.dumps(data1),update=url1)
            em = discord.Embed(description = "Leave message has been set")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
        else:
            em = discord.Embed(description = "There is a leave msg (already set), do you want to change it? Reply yes or no")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
            def check(ctx):
                return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')
            msge = await self.bot.wait_for('message', check=check)
            msge.content = msge.content.lower()
            if msge.content == "yes":
                data["{}".format(server.id)] = {}
                data["{}".format(server.id)]["msg"] = "{}".format(msg)
                data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
                data1["{}".format(server.id)] = {}
                data1["{}".format(server.id)]["set_leave"] = "on"
                url = myjson.store(json.dumps(data),update=url)
                url1 = myjson.store(json.dumps(data1),update=url1)
                em = discord.Embed(description = "Leave message has been set")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "Edit command Terminated :D")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)



    @commands.command(aliases = ["tgwelcome", "tgwel"])
    @commands.check(have_permissions)
    async def togglewel(self,ctx, *,args:str = None):
        '''Toggle leave or not'''
        url = self.toggle_url()
        data = myjson.get(url)
        data = json.loads(data)
        accepted = ["on", "of"]
        if args == None:
            if "{}".format(ctx.guild.id) not in data:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["set_welcome"] = "on"
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Welcome Message Enabled For The Server`")
            else:
                current = data["{}".format(ctx.guild.id)]["set_welcome"]
                await ctx.send("`Welcome messages: {}`".format(current))
        else:
            args = args.lower()
            if args in accepted:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["set_welcome"] = "{}".format(args)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Welcome message set to: {}`".format(args))
            else:
                await ctx.send("`Error: Invalid Parameter, define on or off.`")

    @commands.command(aliases = ["tgleave"])
    @commands.check(have_permissions)
    async def toggleleave(self,ctx, *,args:str = None):
        '''Toggle leave or not'''
        url = self.toggle_url2()
        data = myjson.get(url)
        data = json.loads(data)
        accepted = ["on", "of"]
        if args == None:
            if "{}".format(ctx.guild.id) not in data:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["set_leave"] = "on"
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Leave Message Enabled For The Server`")
            else:
                current = data["{}".format(ctx.guild.id)]["set_leave"]
                await ctx.send("`Leave messages: {}`".format(current))
        else:
            args = args.lower()
            if args in accepted:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["set_leave"] = "{}".format(args)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Leave message set to: {}`".format(args))
            else:
                await ctx.send("`Error: Invalid Parameter, define on or off.`")


    @commands.command(aliases = ["slinks"])
    @commands.check(have_permissions)
    async def storagelinks(self,ctx):
        '''links'''
        url0 = self.load_url()
        url1 = self.toggle_url()
        url2 = self.load_url2()
        url3 = self.toggle_url2()
        await ctx.send("Storage Links:\n1. {} welcome texts.\n2. {} toggle welcome.\n3. {} leave texts.\n4. {} toggle leave.".format(url0, url1, url2, url3))

    @commands.command(aliases = ["weltype"])
    @commands.check(have_permissions)
    async def settype(self,ctx, *,args:str = None):
        '''Toggle pic or text welcome'''
        url = self.msg_type()
        data = myjson.get(url)
        data = json.loads(data)
        accepted = ["pic", "text"]
        if args == None:
            if "{}".format(ctx.guild.id) not in data:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["msg_type"] = "text"
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Welcome Type: TEXT`")
            else:
                current = data["{}".format(ctx.guild.id)]["msg_type"]
                await ctx.send("`Current welcome Type: {}`".format(current))
        else:
            args = args.lower()
            if args in accepted:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["msg_type"] = "{}".format(args)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Welcome type set to: {}`".format(args))
            else:
                await ctx.send("`Error: Invalid Parameter, accepted: pic or text.`")




    async def on_member_join(self,member):
        '''welcome!'''
        try:
            server = member.guild
            user = member
            is_bot = user.bot
            url_toggle = self.toggle_url()
            url_message = self.load_url()
            url_type = self.msg_type()
            data_type = myjson.get(url_type)
            data_type = json.loads(data_type)
            data_toggle = myjson.get(url_toggle)
            data_toggle = json.loads(data_toggle)
            data_message = myjson.get(url_message)
            data_message = json.loads(data_message)
            channel_id = data_message["{}".format(server.id)]["channel_id"]
            msg = data_message["{}".format(server.id)]["msg"]
            channel = self.bot.get_channel(int(channel_id))
            member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
            if data_toggle["{}".format(server.id)]["set_welcome"] == "on" and data_type["{}".format(server.id)]["msg_type"] == "pic":
                #await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number)+"\n**Bot:** {}".format(is_bot))
                url = '{}'.format(member.avatar_url)
            #    print(url)
                response = requests.get(url, stream=True)
                with open('img.png', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                url_ser = '{}'.format(server.icon_url_as(format = 'png'))
                #print(url_ser)
                respon = requests.get(url_ser, stream=True)
                with open('ser.png', 'wb') as ou_file:
                    shutil.copyfileobj(respon.raw, ou_file)
                del respon
                img = Image.open("img.png")
                new_im = Image.new("RGBA", (600,200))
                bg_w, bg_h = new_im.size
                other = Image.open("ser.png")
                other = other.resize((600, 200), PIL.Image.ANTIALIAS)
                other.save('resized_ser.png')
                others = Image.open("resized_ser.png")
                brightness = 0.5
                enhancer = ImageEnhance.Brightness(others)
                others = enhancer.enhance(brightness)
                new_im.paste(others,(0,0))
                img.thumbnail((75,75))
                new_im.paste(img,(42,65))
                font1 = ImageFont.truetype('arialbd.ttf', 25)
                font2 = ImageFont.truetype('Pacifico.ttf',20)
                font3 = ImageFont.truetype('Tabitha.ttf', 22)
                xoff, yoff = (10,5)
                d = ImageDraw.Draw(new_im)
                d.text((149, 31),"Welcome!", fill="white",font = font1)
                t = ImageDraw.Draw(new_im)
                t.text((137, 63),"{}".format(member), fill="white",font = font3)
                m = ImageDraw.Draw(new_im)
                print(len(msg))
                if len(msg)>50:
                    msg = "Have Fun and Enjoy your time in here!"
                else:
                    msg = data_message["{}".format(server.id)]["msg"]
                m.text((136, 80),"{}".format(msg), fill="white",font = font2)
                kk = ImageDraw.Draw(new_im)
                kk.text((137, 109),"Member Number: {}".format(member_number), fill="white",font = font2)
                if is_bot == True:
                    is_bot = "Yes"
                else:
                    is_bot = "No"
                bb = ImageDraw.Draw(new_im)
                bb.text((136, 134),"Bot: {}".format(is_bot), fill="white",font = font2)
                new_im.save("welcome_test.png")
                await channel.send(content = "{0.mention}".format(member),file=discord.File('welcome_test.png'))
            elif data_toggle["{}".format(server.id)]["set_welcome"] == "on" and data_type["{}".format(server.id)]["msg_type"] == "text":
                await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number)+"\n**Bot:** {}".format(is_bot))
        except Exception as e:
            print(e)
            await channel.send("`Error Encountered: {}`".format(e))

    async def on_member_remove(self,member):
        '''Leave!'''
        try:
            server = member.guild
            user = member
            is_bot = user.bot
            url_toggle = self.toggle_url2()
            url_message = self.load_url2()
            data_toggle = myjson.get(url_toggle)
            data_toggle = json.loads(data_toggle)
            data_message = myjson.get(url_message)
            data_message = json.loads(data_message)
            channel_id = data_message["{}".format(server.id)]["channel_id"]
            msg = data_message["{}".format(server.id)]["msg"]
            channel = self.bot.get_channel(int(channel_id))
            #member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
            if data_toggle["{}".format(server.id)]["set_leave"] == "on":
                await channel.send("{}".format(msg)+"\n\n**Member:** {}".format(member.name)+"\n**Server:** **{}**".format(server.name)+"\n**Bot:** {}".format(is_bot)+"\n:wave:")
        except Exception as e:
            #print(e)
            pass

    async def on_guild_join(self, guild):
        try:
            server = guild
            channel = server.text_channels[0]
            msg = "**Thank you for adding me! :slight_smile:\nI am winter-song, and if by mistake I wrote this on an unwanted channel, please forgive me**:sweat_smile:\nTo get started, use **w!help** and you will see all my commands! :dancer:\nYou can also check the website: https://winter-song-web.herokuapp.com/ I hope it's **working** :smile:"
            await channel.send(msg)
        except Exception as e:
            pass




def setup(bot):
	bot.add_cog(Welcomer(bot))
