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
# get the user's username
response = requestSession.get(f"https://users.roblox.com/v1/users/{user_id}")
username = response.json()["name"]
# get the user's friends
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/friends")
friends = response.json()["data"]
# get the user's followers
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/followers")
followers = response.json()["data"]
# get the user's followings
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/followings")
followings = response.json()["data"]
# get the user's friends count
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count")
friends_count = response.json()["count"]
# get the user's followers count
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/followers/count")
followers_count = response.json()["count"]
# get the user's followings count
response = requestSession.get(f"https://friends.roblox.com/v1/users/{user_id}/followings/count")
followings_count = response.json()["count"]