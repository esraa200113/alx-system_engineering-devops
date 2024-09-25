#!/usr/bin/python3
"""
Module to query Reddit API and return the number of subscribers for a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.

    :param subreddit: Name of the subreddit to query.
    :return: Number of subscribers or 0 if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0

