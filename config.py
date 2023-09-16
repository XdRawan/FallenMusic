from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22028862"))
API_HASH = getenv("9ba76f5126553a77b9fe83f995e4709e")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6693204823"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQB-A9W9YK56_SvV8vWaBVut8s38YmLEWaBOBikxdxi9aYdiBOE1UxzDj2b3Y7_5d2L2KoMe8W0jlQHmdtlPi234KYNhkTSP1bz8lVtx5cOqqrfIbXbEp4ibColuF3KXc-TeUn8IJSdMrVLlx3FxyABpQxt6aoVAPlOq9rZeKAimGMZ_FUdcQAILQvI39f6buiUYxkWw8WAZJu-qlndIo0ZFZeard5URb-5IZTrINs9HxGYNt8HNwa4MnmntIMgQwhU92wmK_FK147l9T_iiY2U0KVpLgTQ3m58oDvpJpiqMZf51pquI8LT3KeJbOSRu3D8AfwN0i-h6PsY2T_rECGAAAAAVOCHRkA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
