import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from datetime import datetime
import random

class MyCommands(commands.Cog):
    bypassers = [960542867208675388, 799414495892996116]
    
    def __init__(self, client):
        self.client = client


    @nextcord.slash_command(name="hello", description="A Greeting from the 8Z Bot")
    async def greeting(self, interaction: Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}. What's Up?")

    @nextcord.slash_command(name="copy", description="The bot will copy any phrase.")
    async def echo(self, interaction: Interaction, phrase: str):
        await interaction.response.send_message(f"{interaction.user.mention} said: {phrase}")

    @nextcord.slash_command(name="poll", description="A basic yes/no poll in any given channel.")
    async def poll(self, ctx: Interaction, question: str):
        if ctx.user.guild_permissions.administrator or ctx.user.id in self.bypassers:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            emb = nextcord.Embed(title="POLL", description=f"{question}")
            emb.set_footer(text=f"Poll started by {ctx.user.name} • {current_time}")

            # Send the embed and get the Message object
            msg = await ctx.response.send_message(embed=emb)

            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
        else:
            await ctx.response.send_message(f"{ctx.user.mention} not allowed!!", ephemeral=True)

    @nextcord.slash_command(name="info", description="Gather one's info all in one message.")
    async def info(self, ctx: Interaction, someone: str):
        member = ctx.guild.get_member_named(someone)
        if member:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            emb = nextcord.Embed(title=f"{someone}'s profile")
            emb.set_thumbnail(url=f"{member.display_avatar._url}")


            roles_mentions = [role.mention for role in member.roles]
            roles_str = ", ".join(roles_mentions)
            emb.add_field(name=f"{member.display_name}'s Roles", value=roles_str)

            join_date_str = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
            emb.add_field(name=f"{member.display_name}'s Server Join Date", value=join_date_str)

            emb.set_footer(text=f"Command triggered by {ctx.user.name} • {current_time}")

            await ctx.response.send_message(embed=emb)
        else:
            await ctx.response.send_message(f"Cannot find member named: {someone}", ephemeral=True)

    @nextcord.slash_command(name="roll", description="Roll a dice.")
    async def roll(self, ctx):
        numbers = [1, 2, 3, 4, 5, 6]
        selected_response = random.choice(numbers)
        await ctx.send(f"You rolled: **{selected_response} 🎲**")

    @nextcord.slash_command(name="timetable", description="Check 8Z's timetable straight from google calendar.")
    async def calendar(self, ctx: Interaction, week: str):
        valid_responses = ["A", "B"]

        # Check if the provided week is valid
        if week.upper() in valid_responses:
            if week.upper() == "A":
                emb = nextcord.Embed(title="The timetable for Week A is..")
                emb.add_field(name="Monday", value="Year 8, 8:30am, M202\nEnglish, 8:50am, M212\nMusic, 8:50am, M108\nReligious Education, 11:10am, M114\nArt and Design / Art, 12:10pm, M205\nMathematics, 14:00pm, N/A\nYear 8, 15:00pm, M202")
                emb.add_field(name="Tuesday", value="Year 8, 8:30am, M202\nEnglish, 8:50am, M212\nMathematics, 9:50am, 9:50am, N/A\nSpanish, 11:10am, M117\nScience, 12:10pm, M313\nComputer Science, 14:00pm, M302\nYear 8, 15:00pm, M202")
                emb.add_field(name="Wednesday", value="Year 8, 8:30am, M202\nScience, 8:50am, M313\nSpanish, 9:50am, M117\nPhysical Education / Sports 11:10am - 13:05pm, M001\nMathematics, 14:00pm, N/A")
                emb.add_field(name="Thursday", value="Year 8, 8:30am, M202\nGeography,  8:50am, M114\nDesign and Technology - Food Technology, 9:50am, N/A\nEnglish, 11:10am, M212\nPersonal Social and Health Education (PSHE), 12:10pm, M201\nReligous Education, 14:00pm, M115\nYear 8, 15:00pm, M202")
                emb.add_field(name="Friday", value="Year 8, 8:30am, M202\nSpanish, 8:50am, M117\nEnglish, 9:50am, M124 - CIRCLE\nDrama, 11:10am, M004 - Drama Studio\nHistory, 12:10pm, M115\nScience, 14:00pm, M313\nYear 8, 15:00pm, M202")
                emb.set_footer(text="“Be Careful Who You Trust, Sergeant. People You Know Can Hurt You The Most.” - Ghost")
                await ctx.response.send_message(embed=emb)
            elif week.upper() == "B":
                emb = nextcord.Embed(title="The timetable for Week B is...")
                emb.add_field(name="Monday", value="Year 8, 8:30am, M202\nMusic, 8:50am, M108\nMathematics, 9:50am, N/A\nSpanish, 11:10am, M117\nScience, 12:10, M313\nHistory, 14:00pm, M116\nYear 8, 15:00pm, M202")
                emb.add_field(name="Tuesday", value="Year 8, 8:30am, M202\nReligous Education, M119\nArt and Design / Art, 9:50am, M205\nEnglish, 11:10am, M212\nSpanish, 12:10pm, M117\nMathematics 14:00pm, N/A\nYear 8, 15:00pm, M202")
                emb.add_field(name="Wednesday", value="Year 8, 8:30am, M202\nComputer Science, 8:50am, M302\nScience, 9:50am, M313\nPhysical Education / Sports 11:10am - 13:05pm, M001\nMathematics, 14:00pm, N/A")
                emb.add_field(name="Thursday", value="Year 8, 8:30am, M202\nHistory, 8:50am, M115\nEnglish, M212, 9:50am\nGeography, 11:10am, M114\nDesign and Technology - Food and Technology, 12:10pm, M101\nPersonal Social and Health Education (PSHE), 14:00pm, M201\nYear 8, 15:00pm, M202")
                emb.add_field(name="Friday", value="Year 8, 8:30am, M202\nDrama, M004 - Drama Studio\nSpanish, 9:50am, M117\nGeography. 11:10am, M114\nScience, 12:10pm, M313\nEnglish, 14:00pm, M212\nYear 8, 15:00pm, M202")
                emb.set_footer(text="“Teachers can open the door, but you must enter it yourself.” - Some random guy on google")
                await ctx.response.send_message(embed=emb)
        else:
            await ctx.response.send_message("Invalid input. Please provide 'A' or 'B'.", ephemeral=True)

    @nextcord.slash_command(name="createchannel", description="Lets the bot create a custom channel in a few clicks.")
    async def createchannel(self, ctx: Interaction, channel_name: str):
        if ctx.user.guild_permissions.administrator or ctx.user.id in self.bypassers:
           text_channel = await ctx.guild.create_text_channel(name=channel_name)
           await ctx.response.send_message(f"Successfully created channel: {text_channel.mention}")
        else:
            await ctx.response.send_message(f"{ctx.user.mention} not allowed!!", ephemeral=True)
            


        
def setup(client):
    client.add_cog(MyCommands(client))
