#!/usr/bin/python3
"""
importation
"""
import requests

def number_of_subscribers(subreddit):
    """documentation"""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(reddit_url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
    except Exception:
        pass

    return 0
