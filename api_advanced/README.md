# api_advanced

Python functions that query the Reddit API with the `requests` module.
Each request sends a custom User-Agent and does not follow redirects, so an
invalid subreddit is detected instead of being sent to search results.

## Requirements

- Python 3 with the `requests` module
- Code follows PEP 8

## Files

| File | Function | What it does |
| --- | --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` | Returns the subscriber count, or 0 for an invalid subreddit |
| `1-top_ten.py` | `top_ten(subreddit)` | Prints the first 10 hot post titles, or `None` for an invalid subreddit |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` | Recursively returns a list of all hot post titles, or `None` |
| `3-count.py` | `count_words(subreddit, word_list, after=None, counts=None)` | Recursively counts keywords in hot post titles and prints them sorted |
