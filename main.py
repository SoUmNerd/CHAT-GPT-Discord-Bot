import openai
import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) #Change ! to the command prefix you want
client = discord.Client(intents=intents)

@bot.command()
async def chatgpt(ctx, *, msg=''):
    # Set up the OpenAI API client
    openai.api_key = "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"
    inputdiscord = msg
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
    await ctx.send(response)

bot.run('TOKEN') #CHANGE TO YOUR BOT TOKEN


