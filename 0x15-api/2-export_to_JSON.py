#!/usr/bin/python3
"""Module that exports to JSON from API"""


if __name__ == '__main__':
    from sys import argv
    import requests
    import json

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])

    response_user = requests.get(url_user).json()

    response_tasks = requests.get(url_todos).json()

    with open('{}.json'.format(argv[1]), 'w') as f:
        task_list = []
        for task in response_tasks:
            task_list.append(
                {'completed': task['completed'], 'username': response_user['username'], 'task': task['title']})
        to_json = {argv[1]: task_list}
        json.dump(to_json, f)
