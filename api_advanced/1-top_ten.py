#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import os
import requests

USER_AGENT = "linux:alu.api_advanced:v1.0 (by /u/alu_student)"
TOKEN = {}


def get_response(path, params=None):
    """Fetch a Reddit path, using OAuth when credentials are set."""
    headers = {"User-Agent": USER_AGENT}
    base, suffix = "https://www.reddit.com", ".json"
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    secret = os.environ.get("REDDIT_CLIENT_SECRET")
    if client_id and secret:
        if "value" not in TOKEN:
            auth = requests.post(
                "https://www.reddit.com/api/v1/access_token",
                auth=(client_id, secret), headers=headers,
                data={"grant_type": "client_credentials"})
            TOKEN["value"] = auth.json().get("access_token")
        if TOKEN["value"]:
            headers["Authorization"] = "bearer " + TOKEN["value"]
            base, suffix = "https://oauth.reddit.com", ""
    return requests.get(base + path + suffix, headers=headers,
                        params=params, allow_redirects=False)


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if the subreddit is bad."""
    try:
        response = get_response("/r/{}/hot".format(subreddit),
                                {"limit": 10})
        if response.status_code in (301, 302, 303, 307, 308):
            print(None)
            return
        posts = response.json().get("data", {}).get("children")
    except (requests.RequestException, ValueError, AttributeError):
        print(None)
        return
    if not isinstance(posts, list):
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
