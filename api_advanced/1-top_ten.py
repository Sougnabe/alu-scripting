#!/usr/bin/python3
'''Importation '''
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)
