import tweepy
import requests

api_key = "dRMNi0JD5SgvpYxtd7z6WhCsI"
api_secret = "GsvpGGEkwPPFIXOcF9OhhtYoNTPdzziF91vxpCrFz3zVJsSB69"
access_token = "1524803552383754240-dT6EIXcyYUWmcF30QjjtGbyMgZvB7c"
access_secret = "zU0rv2PnYpsohU5u8uftnsoGxkhJLmAKVwLMLFID6xmUj"
bearer_token = "AAAAAAAAAAAAAAAAAAAAADKQcgEAAAAAoIhdv8QT5jv5qPT%2F96vorDVB%2BCw%3Dez5E3FBoj4Y4cbEaYMcRfocC1xmpb05AfNZ87Nn8vjs1IIAOGY"

client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=api_key,
                       consumer_secret=api_secret,
                       access_token=access_token,
                       access_token_secret=access_secret,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)

usernames = ['wobbly_sausages', 'bigdannydan', 'jakwnd']

for username in usernames:
    user = client.get_user(username=username, user_fields=["name", "username", "location", "verified", "description"])
    json_user = user.json()
    for field in json_user['data']:
        print(field, ': ', json_user['data'][field])