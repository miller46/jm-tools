import discord
import asyncio
from threading import Thread


class DiscordBot:

    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.loop = asyncio.new_event_loop()

        self.client = None

        thread = Thread(target=self.run)
        thread.start()

    def run(self):
        asyncio.set_event_loop(self.loop)
        self.client = discord.Client(intents=discord.Intents.all(), loop=self.loop)

        @self.client.event
        async def on_ready():
            print('Bot is ready.')

        @self.client.event
        async def on_message(message):
            self.on_message(message)

        @self.client.event
        async def on_reaction_add(reaction, user):
            print(f"{user} reacted to a message with {reaction.emoji}")
            pass

        @self.client.event
        async def on_error(event, *args, **kwargs):
            print(f"A Discord bot error occurred: {event}")

        # self.client.run(self.bot_token)
        self.loop.create_task(self.client.start(self.bot_token))
        self.loop.run_forever()

    def on_message(self, message):
        channel_id = message.channel.id
        if message.content.startswith("!hello"):
            self.post_message("test", channel_id)

    def post_message(self, message, channel_id):
        self.loop.call_soon_threadsafe(asyncio.run_coroutine_threadsafe,
                                                   self._async_post_message(message, channel_id),
                                                   self.loop)

    async def _async_post_message(self, message, channel_id):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(channel_id)
        await channel.send(message)

    # NOT WORKING
    def send_webhook_message(self, url, message):
        raise Exception(f"Discord webhooks not working, use post_message instead")
        # self.loop.call_soon_threadsafe(asyncio.run_coroutine_threadsafe,
        #                                            self._async_send_webhook_message(url, message),
        #                                            self.loop)

    # NOT WORKING
    async def _async_send_webhook_message(self, url, message):
        webhook = discord.Webhook.from_url(url)
        await webhook.send(message)

