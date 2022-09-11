#!/usr/bin/python3
"""
Python script to export data in the CSV format.
link: https://www.youtube.com/watch?v=uCv5zGPGgb4&ab_channel=ProCodeTv
link: https://www.adamsmith.haus/python/examples/
      3278/csv-write-to-a-csv-file-and-quote-all-fields
"""

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
