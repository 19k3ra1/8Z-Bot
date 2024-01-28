import nextcord
from nextcord import Intents, Activity, ActivityType
from nextcord.ext import commands
import info

intents = Intents.default()
intents.members = True

client = commands.Bot(intents=intents, status=nextcord.Status.idle)

@client.event
async def on_ready():
    print(f"Success: {client.user.name} is connected to Discord!")
    await update_activity()

async def update_activity():
    await client.wait_until_ready()
    total_members = sum(guild.member_count or 0 for guild in client.guilds)
    activity = Activity(type=ActivityType.watching, name=f"{total_members} 8Z students!")
    
    await client.change_presence(activity=activity)

client.load_extension('commands')
client.run(info.token)