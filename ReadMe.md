# Django Signals

This projects constitutes a basic introduction to Django Signals. Django Signals involve different parts of the application to communicate with each other in a loosely coupled manner. It works using the principle of publsher-subscriber pattern. The publisher part of the application which is often termed as a sender sends out a signal where one or more subscribers, commonly termed as receivers listen for that signal & respond accordingly.

## Table of contents

- About the Project
- Requirements
- Installation

## About the Project

This project involves setting up of profiles for users right after the register. The User Model is the Sender whereas the Profile Model will be the Receiver

## Requirements

This project requires the following modules:

- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Django](https://www.djangoproject.com/)

## Installation

1. Clone the Repo
1. Set up a virtual environment using Python
1. Run pip install requirements.txt
1. Run the local server - python manage.py runserver
