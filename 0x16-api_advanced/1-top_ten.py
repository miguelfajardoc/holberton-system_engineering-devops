#!/usr/bin/python3

from requests import get


def top_ten(subreddit):
    """ print the first 10 hot topics in a subreddit """

    headers = {'User-Agent': 'miky116'}

    req = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
              headers=headers, allow_redirects=False)
    children = {}
    i = 0
    try:
        req = req.json()
#        print(req)
    except:
        return 0
    if "data" in req:
        children = req.get("data").get("children")
        for child in children:
            if i == 9:
                break
            print(child.get("data").get("title"))
            i += 1
    else:
        return 0
