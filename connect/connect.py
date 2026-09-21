from discord.ext import commands
from core import checks


class Connect(commands.Cog):
    """Migrox Support Connect plugin."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="connect")
    @checks.thread_only()
    async def connect(self, ctx):
        await ctx.send("🧡 **MIGROX SUPPORT**\n\nYour support request has been connected.")


def setup(bot):
    bot.add_cog(Connect(bot))
