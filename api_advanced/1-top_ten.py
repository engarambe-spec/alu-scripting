#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu_student)"}


def top_ten(subreddit):
    """Print the first 10 hot titles, or None if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        res = requests.get(url, headers=HEADERS, params={"limit": 10},
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            print(None)
            return
        posts = res.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
