# This example requires the 'message_content' intent.

import discord
import re
from leaderboard import Leaderboard, WordleStats
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

X = 7

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

leaderboard: Leaderboard = Leaderboard()

def secrets():
  file = open('discord-cred.txt', 'r')
  secret = file.read()
  return secret

@client.event
async def on_message(message: discord.Message):
  print(message.author)
  print('Message from {0.author}:\n{0.content}'.format(message))
  newline_separated = message.content.split('\n')
  print(newline_separated)
  match = re.match(r'^Wordle\s\d+,\d+\s(\d|X)/6$', newline_separated[0])
  if message.author == client.user:
    return
  
  if match:
    num_tries = match.group(1)
    num_tries = int(num_tries) if num_tries.isnumeric() else X
    if message.author in leaderboard.user_to_data:
      wordleStats: WordleStats = leaderboard.user_to_data[message.author]
      wordleStats.average = (wordleStats.average * wordleStats.num_solved + num_tries) / (wordleStats.num_solved + 1)
      wordleStats.num_solved += 1
      wordleStats.last_game = datetime.today()

      
    await message.channel.send('Hello!')

client.run(secrets())

def add_colors(colors: dict[str, int], guesses: list[str]):
  for guess in guesses:
    for letter_value in guess:
      match letter_value:
        case '🟩': colors['🟩'] += 1