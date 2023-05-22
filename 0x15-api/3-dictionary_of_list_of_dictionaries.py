#!/usr/bin/python3
"""script to export data in the JSON format
and returns of list of dictionary.
"""

import json
import requests

if __name__ == "__main__":
    base_url = requests.get('https://jsonplaceholder.typicode.com/users')
    users = base_url.json()
    endpoint = requests.get('https://jsonplaceholder.typicode.com/todos')
    task = base_url.json()

    dictionary = {
        str(data.get('id')): [
            {
                'username': data.get('username'),
                'task': item .get('titles'), 'completed':
                    item.get('completed')
            }
            for item in task
            if item.get('userId') == data.get('id')
        ]
        for data in users
    }
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dictionary, json_file)
