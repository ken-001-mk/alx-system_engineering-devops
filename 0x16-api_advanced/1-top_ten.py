#!/usr/bin/python3

"""function that queries the Reddit API
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    if 'data' not in data or 'children' not in data['data']:
        print("None")
        return

    for post in data['data']['children']:
        print(post['data']['title'])
