import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config
import logging

LOGGER = logging.getLogger(__name__)


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ISTKHARAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="ISTKHAR_CHATBOT.idchatbot"),
        )

    async def start(self):
        print("Starting Id chatbot...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("KITTUU_UPDATES")
                await self.one.join_chat("ll_ABOUT_TOXICC_PAPA_ll")
                await self.one.join_chat("FREE_THEMES_TELEGRAM")  # If group exists
            except Exception as e:
                print(f"Join chat error: {e}")

            # User information
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username

            print(f"Id-Chatbot Started as {self.one.me.first_name}")

    async def stop(self):
        LOGGER.info("Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.one.stop()
        except Exception as e:
            LOGGER.error(f"Stop error: {e}")
