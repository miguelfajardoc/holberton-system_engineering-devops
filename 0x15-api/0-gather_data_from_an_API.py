#!/usr/bin/python3

if __name__ == "__main__":
    import json
    from requests import get
    from sys import argv

    user = get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    task = get("https://jsonplaceholder.typicode.com/todos/",
               params={'userId': argv[1]})
    user = user.json()
    task = task.json()

    total = 0
    done = 0
    tasks = []

    for t in task:
        total += 1
        if t["completed"] is True:
            done += 1
            tasks.append(t["title"])

    print("Employee {} is done with task({:d}/{:d}):".format(user["name"],
                                                             done, total))
    for t in tasks:
        print("\t{}".format(t))
