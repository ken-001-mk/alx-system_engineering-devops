#!/usr/bin/python3

"""recursive function that queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
        
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if "error" in data or "data" not in data:
        print("Invalid subreddit or no posts match.")
        return
    
    posts = data["data"]["children"]
    
    for post in posts:
        title = post["data"]["title"].lower()
        
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title and not title.startswith(word_lower + ".") and not title.startswith(word_lower + "!") and not title.startswith(word_lower + "_"):
                if word_lower in counts:
                    counts[word_lower] += 1
                else:
                    counts[word_lower] = 1
    
    if data["data"]["after"] is not None:
        count_words(subreddit, word_list, after=data["data"]["after"], counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        for word, count in sorted_counts:
            print(f"{word}: {count}")
