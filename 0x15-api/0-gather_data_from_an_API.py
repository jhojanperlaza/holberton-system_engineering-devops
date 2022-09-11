#!/usr/bin/python3
""" Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1])

    rq_user_name = requests.get(url_user).json()['name']
    rq_todos = requests.get(url_todos).json()

    task_title = []
    all_tasks = 0
    completed_tasks = 0

    for element in rq_todos:
        if element['userId'] == int(sys.argv[1]):
            all_tasks += 1
            if element['completed'] is True:
                completed_tasks += 1
                task_title.append(element['title'])
    print("Employee {} is done with tasks({}/{}):".format(rq_user_name,
          completed_tasks, all_tasks))
    print("\t{}".format('\n\t'.join(map(str, task_title))))
