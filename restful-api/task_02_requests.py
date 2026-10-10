#!/usr/bin/python3
"""Module for consuming and processing posts from an API."""

import csv

import requests


def fetch_and_print_posts():
    """Fetches all posts from API and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches all posts from API and saves them to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=url)

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["id", "title", "body"])
            for post in posts:
                writer.writerow([
                    post.get("id"), 
                    post.get("title"), 
                    post.get("body")
                ])


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
