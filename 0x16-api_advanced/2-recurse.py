#!/usr/bin/python3

from requests import get


def recurse(subreddit, hot_list=[]):
    """ print the first 10 hot topics in a subreddit """

    next = {'after': None}
    hot_list = []

    recurse_param(subreddit, next, hot_list)
    return hot_list


def recurse_param(subreddit, next, hot_list):
    """ recursion function """

    headers = {'User-Agent': 'miky116'}

    req = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
              headers=headers, params=next, allow_redirects=False)
    children = {}
    try:
        req = req.json()
    except:
        print(None)
        return
    if "data" in req and "children" in req.get("data"):
        children = req.get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        if req.get("data").get("after") is None:
            return hot_list
        else:
            next["after"] = req.get("data").get("after")
            hot_list = recurse_param(subreddit, next, hot_list)
    else:
        print(None)
        return
