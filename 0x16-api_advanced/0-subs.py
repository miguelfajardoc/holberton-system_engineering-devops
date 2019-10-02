#!/usr/bin/python3

from requests import get


def number_of_subscribers(subreddit):
    """ return the number of subscribers in a subreddit """

    headers = {'User-Agent': 'miky116'}

    req = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
              headers=headers, allow_redirects=False)
    dat = {}
    try:
        req = req.json()
    except:
        return 0
    if "data" in req:
        dat = req["data"]
        if "subscribers" in dat:
            return dat["subscribers"]
        else:
            pass
    else:
        pass
    return 0
