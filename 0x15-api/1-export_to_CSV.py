#!/usr/bin/python3
"""Module that exports to csv from API"""


if __name__ == '__main__':
    from sys import argv
    import requests
    import csv

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])

    response_user = requests.get(url_user).json()

    response_tasks = requests.get(url_todos).json()

    with open('{}.csv'.format(argv[1]), 'w') as f:
        to_csv = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in response_tasks:
            row = [response_user['id'], response_user['username'],
                   task['completed'], task['title']]
            to_csv.writerow(row)
