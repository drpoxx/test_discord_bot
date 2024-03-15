import discord
from .logger import configure_logging
# from discord import Intents, Client, Message
from .responses import get_response

# intents: Intents = Intents.default()
# intents.message_content = True
# client: Client = Client(intents=intents)

# print(type(Intents.default()))

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.logging = configure_logging()

    async def on_ready(self) -> None:
        self.logging.info(f"Logged in as {self.user}")

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return 

        self.logging.info(f"Message from {message.author} in {message.channel}: {message.content}")
        await self.send_message(message=message, user_message=message.content)

    async def send_message(self, message, user_message) -> None:
        if not message:
            self.logging.warning("Message was empty because intents were not enabled properly")
            return None
        
        # If messages start with a question mark the bot messages the user privately.
        if is_private := user_message[0] == "?":
            user_message = user_message[1:]

        try: 
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            self.logging.exception(e)

