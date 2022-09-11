#!/usr/bin/python3
"""  Python script to export data in the JSON format"""

import json
import requests


if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/'

    rq_user_name = requests.get(url_user).json()
    rq_todos = requests.get(url_todos).json()

    format_save = {}
    list_save = []
    dict_save = {}

    for user in rq_user_name:

        for element in rq_todos:
            dict_save = {
                    'username': user.get('username'),
                    'task': element.get('title'),
                    'completed': element.get('completed'),
                    }
            list_save.append(dict_save)
        format_save[user.get('id')] = list_save

    with open("todo_all_employees.json", 'w') as file:
        str_json = json.dumps(format_save)
        file.write(str_json)
