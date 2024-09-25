#!/usr/bin/python3
"""
2-main: Test module for recurse function.
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))  # Print the number of titles fetched
        else:
            print("None")

