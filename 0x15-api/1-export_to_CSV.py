#!/usr/bin/python3
"""Script to export data in the CSV format."""

import requests
import sys
import csv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(base_url + 'users/{}'.format(userId)).json()
    todo = requests.get(base_url + 'todos?userId={}'.format(userId)).json()

    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        write_to_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            write_to_file.writerow([int(userId), user.get(
                'username'), task.get('completed'), task.get('title')])
