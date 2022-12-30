import asyncio
from os import environ

from twitchAPI.twitch import Twitch
from dotenv import load_dotenv

async def getStreams(user_id: str):
    twitch = await Twitch(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'))

    streams = twitch.get_streams(user_id=[user_id])
    async for fields in streams.__aiter__():
        print("All stream information:\n\n", fields.to_dict())

def main():
    load_dotenv('../.env')
    asyncio.run(getStreams('106159308'))

if __name__ == "__main__":
    main()