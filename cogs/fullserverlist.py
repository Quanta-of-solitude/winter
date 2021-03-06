'''
List of servers the bot is in.
'''

from operator import itemgetter
import json
import requests
from discord.ext import commands
import re
import string



class ServerList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def serverlistget(self):
        servers = []
        servercount = 0
        servlist = []
        online = ['online','idle','dnd','do_not_disturb']
        totalmemcount = 0
        for server in self.bot.guilds:
            memcount = 0
            servercount += 1
            for member in server.members:
                if str(member.status) != 'offline' and member.bot != True:
                    memcount += 1
                    totalmemcount += 1

            servlist.append({'name': server.name, 'online': memcount, 'id': server.id})
        servlist = sorted(servlist, key=itemgetter('online'), reverse=True)

        for server in servlist:
            server['name'] = ''.join(filter(lambda x: x in string.printable, server['name']))
            servers.append(str(server['online']).zfill(2) + ' ' + server['name'].replace('`',''))
        servers = '\n'.join(servers)
        return '```python\nServer List -- servers(' + str(servercount) + ') online(' + str(totalmemcount) +') members.\n' + str(servers) + '\n```'

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['fullserver', 'fsvrlist', 'flists'])
    async def fullserverlist(self,ctx):
        try:
            if ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
                servers = self.serverlistget()
                try:
                    out = await ctx.send(servers)
                except:
                    paginated_text = ctx.paginate(servers)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'\n{page}\n')
                            break
                        await ctx.send(f'\n{page}\n')
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(ServerList(bot))
