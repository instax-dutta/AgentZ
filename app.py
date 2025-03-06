import os
import requests
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import traceback
import logging
import asyncio
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('SecretAgentBot')

# Load environment variables
load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
GUILD_ID = int(os.getenv('GUILD_ID'))  # Specific guild ID
ALLOWED_CHANNEL_ID = int(os.getenv('ALLOWED_CHANNEL_ID'))  # Specific channel ID
AGENT_ID = os.getenv('AGENT_ID')  # Your agent ID

# Initialize uptime tracking
start_time = time.time()

class SecretAgentBot(commands.Bot):
    def __init__(self):
        # Set up intents
        intents = discord.Intents.default()
        intents.message_content = True
        
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        """
        Setup hook for command registration
        """
        # Get the specific guild
        guild = discord.Object(id=GUILD_ID)
        
        try:
            # Clear existing commands for this guild
            self.tree.clear_commands(guild=guild)
            
            # Sync commands for the specific guild
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            
            logger.info(f"Commands synchronized for guild {GUILD_ID}")
        except Exception as e:
            logger.error(f"Failed to register commands: {e}")
            logger.error(traceback.format_exc())

    async def generate_secret_agent_response(self, prompt):
        """Generate a secret agent-style response using Mistral API"""
        try:
            # Prepare the request payload
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 500,
                "agent_id": AGENT_ID
            }
            
            # Set API endpoint and headers
            url = "https://api.mistral.ai/v1/agents/completions"
            headers = {
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # Make the API request
            response = requests.post(url, json=payload, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                logger.error(f"API Error: {response.status_code} - {response.text}")
                return f"Transmission error. Secure line compromised. Details: {response.status_code}"
        except Exception as e:
            logger.error(f"API Error: {e}")
            return f"Transmission error. Secure line compromised. Details: {str(e)}"

# Create bot instance
bot = SecretAgentBot()

@bot.tree.command(name="mission", description="Submit a classified query to Agent Z")
async def mission_command(interaction: discord.Interaction, query: str):
    """
    Slash command to interact with the secret agent bot
    Restricted to a specific channel
    """
    # Check if command is in the allowed channel
    if interaction.channel_id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message(
            "⚠️ Unauthorized access point. Mission can only be initiated in the designated secure channel.", 
            ephemeral=True
        )
        return

    # Defer initial response
    await interaction.response.defer()
    
    # Generate secret agent response
    response = await bot.generate_secret_agent_response(query)
    
    # Craft a secret agent style message
    encoded_response = f"🕵️ **CONFIDENTIAL TRANSMISSION** 🕵️\n```\n{response}\n```\n*This message will self-destruct in 60 seconds.*"
    
    # Send the message
    message = await interaction.followup.send(encoded_response)
    
    # Delete the message after 60 seconds
    await asyncio.sleep(60)
    await message.delete()

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping_command(interaction: discord.Interaction):
    """
    Slash command to check the bot's latency
    """
    latency = bot.latency * 1000  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! 🏓 Latency: {latency:.2f} ms")

@bot.tree.command(name="uptime", description="Check the bot's uptime")
async def uptime_command(interaction: discord.Interaction):
    """
    Slash command to check the bot's uptime
    """
    uptime = time.time() - start_time
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    await interaction.response.send_message(f"Uptime: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")

@bot.event
async def on_ready():
    """Bot ready event"""
    logger.info(f"Agent {bot.user} is active. Awaiting classified instructions.")
    logger.info(f"Connected to {len(bot.guilds)} guilds")
    
    # Verify channel and guild configuration
    try:
        guild = bot.get_guild(GUILD_ID)
        channel = guild.get_channel(ALLOWED_CHANNEL_ID)
        
        if not guild:
            logger.error(f"Cannot find guild with ID {GUILD_ID}")
        if not channel:
            logger.error(f"Cannot find channel with ID {ALLOWED_CHANNEL_ID}")
    except Exception as e:
        logger.error(f"Error verifying guild/channel: {e}")

def main():
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()