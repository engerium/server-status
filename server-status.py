#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Imports
import requests
import os

# Constants
MAILGUN_API_URL = "https://api.mailgun.net/v3/domain.com/messages"
MAILGUN_API_KEY = "key-xxxxxxxxxxxxxxxxxxxx"

HOST = "x.x.x.x"

SENDER = "Administrator <administrator@domain.com>"
RECIPIENTS = ["user@gmail.com"]
SUBJECT = "[ALERT] Servers Unreachable"
MESSAGE = "This is an auto generated notification. Please contact the server administrator for more details."

# Mailgun send email function
def send_simple_message(api, recipient, subject, message):
    return requests.post(
        MAILGUN_API_URL,
        auth=("api", api),
        data={"from": SENDER,
              "to": recipient,
              "subject": subject,
              "text": message})


# Ping funtion
def ping(host):
	# Ping host system
	response = os.system("ping -c 1 " + host)

	# Return true if reachable, false if unreachable
	if response == 0:
		return True
	else:
		return False

# Main function
def main():
	# If ping not reachable
	if not ping(HOST):
		send_simple_message(MAILGUN_API_KEY, RECIPIENTS, SUBJECT, MESSAGE)


# Calling of main function
if __name__ == '__main__':
	main()