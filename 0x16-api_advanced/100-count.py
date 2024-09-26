#!/usr/bin/python3
"""
Module to query the Reddit API recursively, parse titles of hot articles,
and count specific keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    """
    Queries the Reddit API recursively, counts occurrences of keywords in titles of
    hot articles, and prints the results in descending order of count.

    :param subreddit: The subreddit to query.
    :param word_list: List of keywords to count in the article titles.
    :param hot_list: List of hot article titles (used for recursion).
    :param after: The token for pagination (used for recursion).
    :param counts: Dictionary to store keyword counts.
    :return: Prints the counts sorted by occurrences and then alphabetically.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    params = {'limit': 100, 'after': after}
    
    word_list = [word.lower() for word in word_list]  # Case-insensitive keywords

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Handle valid responses
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            # Iterate over each post and count keyword occurrences in titles
            for post in posts:
                title = post.get('data', {}).get('title', '').lower()
                for word in word_list:
                    # Count word occurrences in the title
                    count = title.split().count(word)
                    if count > 0:
                        counts[word] = counts.get(word, 0) + count

            # Recursion: If there's more data (pagination), continue
            if after is not None:
                return count_words(subreddit, word_list, hot_list, after, counts)
            else:
                # Once recursion ends, sort and print the results
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda kv: (-kv[1], kv[0])
                )
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")

        else:
            return None  # Invalid subreddit, print nothing

    except requests.RequestException:
        return None  # Handle request errors gracefully

