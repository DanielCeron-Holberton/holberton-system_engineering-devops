#!/usr/bin/python3
"""Module to consume API"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])

    response_user = requests.get(url_user).json()

    response_tasks = requests.get(url_todos).json()

    tasks_done = []

    for task in response_tasks:
        if task['completed']:
            tasks_done.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        response_user['name'], len(tasks_done), len(response_tasks)))
    print("\n".join("\t {}".format(task) for task in tasks_done))
