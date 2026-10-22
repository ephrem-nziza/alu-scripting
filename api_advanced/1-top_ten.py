#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if the subreddit is bad."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    try:
        response = requests.get(url, headers=headers,
                                params={"limit": 10}, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
