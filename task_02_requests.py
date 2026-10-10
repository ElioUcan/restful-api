#!/usr/bin/python3

import requests
import json
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=url)
    print(response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=url)

    if response.status_code == 200:
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'title', 'body'])
            for post in posts:
                writer.writerow([post.get("id"), post.get("title"), post.get("body")])

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
