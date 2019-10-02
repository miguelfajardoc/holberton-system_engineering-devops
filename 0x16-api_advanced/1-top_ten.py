#!/usr/bin/python3

from requests import get


def top_ten(subreddit):
    """ print the first 10 hot topics in a subreddit """

    headers = {'User-Agent': 'miky116'}
    load = {'limit': 10}
    req = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
              headers=headers, params=load, allow_redirects=False)
    children = {}
    i = 0
    try:
        req = req.json()
    except:
        print(None)
        return
    if "data" in req and "children" in req.get("data"):
        children = req.get("data").get("children")
        for child in children:
            print(child.get("data").get("title"))
    else:
        print(None)
        return
