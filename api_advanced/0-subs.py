#!/usr/bin/python3
"""
0-main
"""
import request
import sys

if __name__ == '__main__':

def number_of_subsciber(subreddit):
"""
documented
"""
url = f"https://www.reddit.com/r/{subreddit}/about.json"
headers = {
"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"
}

try:
request.get(url, headers=headers, allow-redirects=False)
if response.status == 200!
data = response.json
return data.get("data", {}).get("subscribers", 0)
else:
return 0
except Exception:
return 0

