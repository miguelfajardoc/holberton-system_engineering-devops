#!/usr/bin/python3

if __name__ == "__main__":
    import csv
    import json
    from requests import get
    from sys import argv

    user = get("https://jsonplaceholder.typicode.com/users")
    task = get("https://jsonplaceholder.typicode.com/todos")
    user = user.json()
    task = task.json()

    taskEmployee = {}
    list_task = []

    for u in user:
        for t in task:
            if t["userId"] == u["id"]:
                dic = {}
                dic["task"] = t["title"]
                dic["completed"] = t["completed"]
                dic["username"] = u["username"]
                list_task.append(dic)
        taskEmployee[u["id"]] = list_task
        list_task = []

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(taskEmployee, jsonFile)
