#!/usr/bin/python3
"""Module that exports to JSON from API"""


from urllib import request


if __name__ == '__main__':
    import requests
    import json

    def request_function(id):

        url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)

        response_user = requests.get(url_user).json()

        response_tasks = requests.get(url_todos).json()

        task_list = []
        if response_user:
            for task in response_tasks:
                task_list.append(
                    {'completed': task['completed'],
                     'username': response_user['username'], 'task': task['title']})
                to_json = {id: task_list}
            return to_json
        return None
    id = 1
    dict_json = {}
    to_json = request_function(id)
    while(to_json):
        dict_json.update(to_json)
        id += 1
        to_json = request_function(id)
    with open("todo_all_employees.json", "w") as f:
        json.dump(dict_json, f)
