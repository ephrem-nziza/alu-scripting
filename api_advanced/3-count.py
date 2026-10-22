#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def print_counts(word_list, counts):
    """Print keyword totals, highest first, ties sorted A to Z."""
    words = [w.lower() for w in word_list]
    totals = {}
    for word in set(words):
        total = counts.get(word, 0) * words.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda i: (-i[1], i[0])):
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles."""
    first_call = counts is None
    if first_call:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            if not first_call:
                print_counts(word_list, counts)
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        if not first_call:
            print_counts(word_list, counts)
        return

    keywords = set(w.lower() for w in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for word in title.lower().split():
            if word in keywords:
                counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after is None:
        print_counts(word_list, counts)
        return
    count_words(subreddit, word_list, after, counts)
