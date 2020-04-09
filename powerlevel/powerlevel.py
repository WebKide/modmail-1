from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

levels = {};
def setup(maxLevel):
  for i in range(1, maxLevel+1):
    levels[i] = " [⚡" + str(i) + "]";

# Setup
setup(140)

class PowerLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def powerlevel(self, ctx, *, content:str):
        # Vars
        guild   = ctx.message.guild;
        user_id = ctx.message.author.id;
        error   = "**<@" + str(user_id) + ">, per favore inserisci un power level valido.**"
        if content.isdigit():
            # Vars
            index  = int(content);
            member  = guild.get_member(user_id)
            # Check
            await ctx.send(member.nick)
            await ctx.send(content)
            # New Nickname
            if index > 0 and index <= 140:
                tag = levels[index];  
                await ctx.send('Hii')
                await ctx.send(tag)
                # New Nickname
                await member.edit(nick='Ciaooo')
                # Reaction
                await ctx.message.add_reaction('✅')
            else:
                await ctx.send(error)
        else:
           await ctx.send(error)
         
        
def setup(bot):
    bot.add_cog(PowerLevel(bot))
