import discord
from src.bot import MyClient
from src.utils import fetch_token

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    token = fetch_token()
    client.run(token=token)


if __name__ == "__main__":
    main()
