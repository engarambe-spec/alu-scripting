#!/usr/bin/python3
"""Recursively collect the titles of all hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu_student)"}


def recurse(subreddit, hot_list=None, after=None):
    """Return all hot post titles, or None if subreddit is invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        res = requests.get(url, headers=HEADERS, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return None
        data = res.json().get("data", {})
    except Exception:
        return None
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
