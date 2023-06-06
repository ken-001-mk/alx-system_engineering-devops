#!/usr/bin/python3

"""recursive function that returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    
    headers = {'User-Agent': 'Recursive Reddit Scraper'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        if len(posts) == 0:
            return hot_list if hot_list else None
        
        for post in posts:
            hot_list.append(post['data']['title'])
        
        after = data['data']['after']
        
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"An error occurred: {response.status_code}")
