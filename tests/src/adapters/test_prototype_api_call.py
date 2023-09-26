import requests as r
import os
from dotenv import load_dotenv
load_dotenv()
cookie = os.getenv("ROBLOSECURITY_COOKIE_09_26")

# initiate a session
requestSession = r.Session()
requestSession.cookies[".ROBLOSECURITY"] = cookie

# get the user's id
response = requestSession.get("https://www.roblox.com/mobileapi/userinfo")
user_id = response.json()["UserID"]
assert user_id == 5067845487