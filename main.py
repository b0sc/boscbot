from functools import reduce
import discord
import os

from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

MY_GUILD = discord.Object(id=937721195166568529)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


client = MyClient(intents=intents)

# client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   if message.content.startswith('/hello'):
#     await message.channel.send(
#         'Hello! im an open source bot made by @lyte for Birendra Open Source Club. Feel free to use me for your own purposes. Thanks!'
#     )


@client.tree.command(description="Classic ping pong game")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


@client.tree.command(description="Say hello to us.")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Hello! im an open source bot made by @lyte for Birendra Open Source Club. "
        "Feel free to use me for your own purposes. Thanks!"
    )


@client.tree.command(description="Let's calculate the factorial")
@app_commands.describe(
    number="The number to calculate factorial of.",
)
async def factorial(interaction: discord.Interaction, number: int):
    await interaction.response.send_message(
        f"The factorial of {number} is {calculate_factorial(number)}"
    )


def calculate_factorial(number: int):
    return reduce(lambda x, y: x * y, range(1, number + 1))


@client.tree.command(description="A gift to you from BOSC")
async def get_nitro(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Rickroll",
        description="Get rickrolled",
        color=0x00FF00,
    ).set_image(url="https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")

    await interaction.response.send_message(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", embed=embed, ephemeral=True
    )


client.run(os.getenv("TOKEN"))
