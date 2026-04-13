import discord
import json

info = json.load(open("json/info.json", "r", encoding="utf-8_sig"))

class Main(discord.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            intents=intents,
        )
        
        load_commands = ["general", "admin_only"]
        for cmd in load_commands:
            try:
                self.load_extension(f"my_commands.{cmd}")
                print(f"[init] {cmd} loaded")
            except Exception as e:
                print(f"[init] {cmd} load failed: {e}")

            
    async def on_ready(self):
        print("Login!")
        print(self.user.id)
        print('------')

bot = Main()
bot.run(info["discord_token"])