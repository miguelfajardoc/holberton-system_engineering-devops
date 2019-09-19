#!/usr/bin/python3

if __name__ == "__main__":
    import csv
    import json
    from requests import get
    from sys import argv

    user = get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    task = get("https://jsonplaceholder.typicode.com/todos/",
               params={'userId': argv[1]})
    user = user.json()
    task = task.json()

    taskEmployee = {}
    list_task = []

    for t in task:
        dic = {}
        dic["task"] = t["title"]
        dic["completed"] = t["completed"]
        dic["username"] = user["username"]
        list_task.append(dic)

    taskEmployee[argv[1]] = list_task

    with open(argv[1] + '.json', 'w') as jsonFile:
        json.dump(taskEmployee, jsonFile)
