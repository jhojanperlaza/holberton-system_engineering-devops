#!/usr/bin/python3
"""  Python script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        2)

    rq_user_name = requests.get(url_user).json()['username']
    rq_todos = requests.get(url_todos).json()

    format_save = {}
    list_save = []
    dict_save = {}

    for element in rq_todos:
        if element['userId'] == int(2):
            dict_save = {
                'task': element['title'],
                'completed': element['completed'],
                'username': rq_user_name
                }
            list_save.append(dict_save)

    format_save[2] = list_save

    with open("{}.json".format(2), 'w',) as file:
        str_json = json.dumps(format_save)
        file.write(str_json)
