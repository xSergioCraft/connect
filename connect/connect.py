import discord
from discord.ext import commands
from core import checks


class Connect(commands.Cog):
    """Migrox Support Connect plugin."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="connect")
    @checks.thread_only()
    async def connect(self, ctx):
        message = (
            "**🧡 MIGROX SUPPORT**\n\n"
            "**Your support request has been connected.**\n\n"
            "A member of the **Migros Corporation Support Team** "
            "is now connected to your request and will assist you shortly.\n\n"
            "**👤 Support Representative**\n"
            f"{ctx.author.mention}\n\n"
            "**🕒 Connected**\n"
            f"{discord.utils.utcnow().strftime('%d %B %Y • %H:%M UTC')}\n\n"
            "**📌 Please Note**\n"
            "Please remain in this conversation while your request "
            "is being handled by our Support Team."
        )

        ctx.message.content = message

        async with ctx.typing():
            await ctx.thread.reply(ctx.message)


async def setup(bot):
    await bot.add_cog(Connect(bot))
