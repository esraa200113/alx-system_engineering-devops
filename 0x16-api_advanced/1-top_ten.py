#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot posts for a given subreddit.
If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None.

    :param subreddit: Name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)

