from discord.ext import commands
import discord


class Shiki(commands.Bot):
    def __init__(self, *args, **kwargs):
        kwargs["command_prefix"] = "s!"
        intents = discord.Intents.default()
        intents.members = True
        kwargs["intents"] = intents
        super().__init__(*args, **kwargs)