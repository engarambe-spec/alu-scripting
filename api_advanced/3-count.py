#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests

HEADERS = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu_student)"}


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of each keyword found in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        res = requests.get(url, headers=HEADERS, params=params,
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return
        data = res.json().get("data", {})
    except Exception:
        return
    for child in data.get("children", []):
        title = child.get("data", {}).get("title") or ""
        for word in title.lower().split():
            counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    totals = {}
    for word in word_list:
        word = word.lower()
        totals[word] = totals.get(word, 0) + counts.get(word, 0)
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        if total > 0:
            print("{}: {}".format(word, total))
