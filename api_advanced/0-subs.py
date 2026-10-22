#!/usr/bin/python3
"""Query the Reddit API for the subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return 0
    return data.get("subscribers", 0)
