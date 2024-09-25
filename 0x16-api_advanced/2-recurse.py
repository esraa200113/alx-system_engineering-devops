#!/usr/bin/python3
"""
Module to query the Reddit API recursively and return all hot article titles
for a given subreddit.
"""

import requests
import time


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit.

    :param subreddit: The subreddit to query.
    :param hot_list: The list of hot article titles (used for recursion).
    :param after: The token for pagination (used for recursion).
    :return: List of hot article titles, or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')  # Token for next page

            # Extend hot_list with current page's titles
            hot_list.extend([post.get('data', {}).get('title') for post in posts])

            # If there is more data to fetch (pagination), recurse
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 429:
            # Handle Reddit rate limiting (status code 429), wait and retry
            print("Rate limited by Reddit API. Waiting 60 seconds...")
            time.sleep(60)
            return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

