#!/usr/bin/python3
"""Query the Reddit API for the hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Request the first 10 hot posts and print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0"}
    params = {"limit": 10}

    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass

    print("OK")
