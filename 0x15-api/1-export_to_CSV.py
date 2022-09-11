#!/usr/bin/python3
""" Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

import csv
import requests
import sys

if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1])

    rq_user_name = requests.get(url_user).json()['username']
    rq_todos = requests.get(url_todos).json()

    format_save = []

    for element in rq_todos:
        if element['userId'] == int(sys.argv[1]):
            string_save = '{},{},{},{}'.format(
                element['userId'], rq_user_name,
                element['completed'], element['title'])
            format_save.append(string_save.split(','))

    with open("{}.csv".format(sys.argv[1]), 'w',) as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(format_save)
