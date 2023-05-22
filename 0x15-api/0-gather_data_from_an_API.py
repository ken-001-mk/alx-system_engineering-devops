#!/usr/bin/python3
"""Script for getting data from API placeholder."""

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(base_url + 'users/{}'.format(userId)).json()
    todo = requests.get(base_url + 'todos?userId={}'.format(userId)).json()
    completed = []

    for task in todo:
        if task.get("completed"):
            completed.append(task.get("title"))
    print("Employee {} is done with task({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    for task in completed:
        print('\t', task)
