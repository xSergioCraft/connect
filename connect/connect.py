import discord
from discord.ext import commands

from core import checks


class Connect(commands.Cog):
    """Migrox Support Connect plugin for Modmail 4.0.0."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="connect",
        description="Connect to the current Modmail ticket."
    )
    @checks.thread_only()
    async def connect(self, ctx):
        """Send the Migrox Support connection message to the user."""

        embed = discord.Embed(
            title="🧡 MIGROX SUPPORT",
            description=(
                "**Your support request has been connected.**\n\n"
                "A member of the **Migros Corporation Support Team** "
                "is now connected to your request and will assist you shortly."
            ),
            colour=discord.Colour.orange()
        )

        embed.add_field(
            name="👤 Support Representative",
            value=ctx.author.mention,
            inline=False
        )

        embed.add_field(
            name="🕒 Connected",
            value=discord.utils.utcnow().strftime(
                "%d %B %Y • %H:%M UTC"
            ),
            inline=False
        )

        embed.add_field(
            name="📌 Please Note",
            value=(
                "Please remain in this channel while your request "
                "is being handled by our Support Team."
            ),
            inline=False
        )

        embed.set_footer(
            text="Migros Corporation • Migrox Support"
        )

        # Send the response through Modmail's thread system.
        await ctx.thread.reply(embed=embed)


def setup(bot):
    bot.add_cog(Connect(bot))
