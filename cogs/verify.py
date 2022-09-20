from discord.ext import commands
from discord import app_commands
import discord


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="verify", description="Verify account")
    async def verify(self, interaction: discord.Interaction, role: discord.Role):
        