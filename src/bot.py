from discord import Intents, Client, Message
from responses import get_response

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

print(type(Intents.default()))

async def send_message(message: Message, user_message: str) -> None:
    if not message:
        print("Message was empty because intents were not enabled properly")
        return None
    # If messages start with a question mark the bot messages the user privately.
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try: 
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)