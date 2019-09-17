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

    with open(argv[1] + '.csv', 'w') as csvFile:
        csvFile = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)

        for t in task:
            csvFile.writerow([argv[1], user["name"], t["completed"],
                              t["title"]])
