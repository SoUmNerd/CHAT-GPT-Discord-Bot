import openai
import discord
from discord import app_commands



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name='chatgpt', description='Chat GPT on discord.')
async def chatgpt(interaction: discord.Interaction, input: str):
    await interaction.response.defer()
    # Set up the OpenAI API client
    openai.api_key = "api-key" #Change this
    inputdiscord = input
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = (inputdiscord)
    # Generate a response
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )
    response = completion.choices[0].text
    await interaction.followup.send(response)

client.run('TOKEN') #CHANGE TO YOUR BOT TOKEN
