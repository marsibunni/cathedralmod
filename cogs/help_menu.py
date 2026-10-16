
from pathlib import Path

import discord
from discord.ext import commands

BANNER = Path(__file__).resolve().parent.parent / "assets" / "cathedral_banner.png"


class HelpMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_menu(self, ctx, *, command_name: str = None):
        if command_name:
            command = self.bot.get_command(command_name)

            if command is None or command.hidden:
                return await ctx.send("✧ Couldn't find that command, silly.")

            usage = f"{ctx.prefix}{command.qualified_name} {command.signature}".strip()

            embed = discord.Embed(
                title=f"✧ {command.qualified_name}",
                description=(
                    f"**Usage**\n`{usage}`\n\n"
                    f"{command.help or command.brief or 'A little CathedralMod utility.'}"
                ),
                color=0x83B7FF,
            )
            embed.set_footer(text="CathedralMod • by Marsi")
            return await ctx.send(embed=embed)

        embed = discord.Embed(
            title="✧ CathedralMod",
            description="your server's prettiest little menace 🦋",
            color=0x83B7FF,
        )

        embed.add_field(
            name="✦ Moderation",
            value="`ban` · `kick` · `mute` · `unmute`",
            inline=False,
        )
        embed.add_field(
            name="☾ Channel Controls",
            value="`lock` · `unlock` · `slowmode`",
            inline=False,
        )
        embed.add_field(
            name="✧ Warnings",
            value="`warn` · `warnings`",
            inline=False,
        )
        embed.add_field(
            name="🦋 Filtering & Cleanup",
            value="`purge` · `/filter add` · `/filter remove` · `/filter list`",
            inline=False,
        )
        embed.add_field(
            name="⌑ Need a little guidance?",
            value=(
                f"Try `{ctx.prefix}help ban` for individual commands.\n"
                "Prefixes: `$` and `!`"
            ),
            inline=False,
        )

        embed.set_footer(text="CathedralMod • by Marsi")

        if BANNER.is_file():
            attachment = discord.File(BANNER, filename="cathedral_banner.png")
            embed.set_image(url="attachment://cathedral_banner.png")
            await ctx.send(embed=embed, file=attachment)
        else:
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(HelpMenu(bot))
