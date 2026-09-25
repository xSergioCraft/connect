import discord
from discord.ext import commands
from core import checks


class Connect(commands.Cog):
    """Migrox Support Partnerships info plugin."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="partnershipsrequirements")
    @checks.thread_only()
    async def connect(self, ctx):
message = (
    "**🧡 MIGROS CORPORATION — PARTNERSHIPS**\n\n"
    "We are pleased to consider partnership opportunities with "
    "**Migros Corporation**. To ensure that our partnerships are "
    "beneficial and sustainable for both communities, all prospective "
    "partners must meet the following requirements.\n\n"

    "**📋 Partnership Requirements**\n\n"
    "• Your Discord server must have at least **40 members**.\n"
    "• Your organization must have an active **Roblox group** with at least **20 members**.\n"
    "• You must **not sell MR+ ranks or community ownership**.\n"
    "• You must be able to provide at least **2 Affiliate Representatives** to work with our team.\n"
    "• You must be able to **regularly promote and post our server advertisement** within your community.\n\n"

    "**🤝 Interested in Partnering?**\n\n"
    "If your organization meets **all of the requirements above** "
    "and you would like to establish a partnership with **Migros Corporation**, "
    "please confirm below you want to continue..\n\n"

    "Our **Public Affairs Team** will review your request and guide you "
    "through the partnership process.\n\n"

    "**Migros Corporation**\n"
    "*Building connections. Growing together.* 🧡"
)

        ctx.message.content = message

        async with ctx.typing():
            await ctx.thread.reply(ctx.message)


async def setup(bot):
    await bot.add_cog(Connect(bot))
