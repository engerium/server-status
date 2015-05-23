#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Imports
import requests
import os
import socket

# Constants
MAILGUN_API_URL = "https://api.mailgun.net/v3/domain.com/messages"
MAILGUN_API_KEY = "key-xxxxxxxxxxxxxxxxxxxx"

HOST = "x.x.x.x"

SENDER = "Administrator <administrator@domain.com>"
RECIPIENTS = ["user@gmail.com"]
FOOTER = "This is an auto generated notification. Please contact the server administrator for more details."


# Mailgun send email function
def send_email(api, recipient, subject, message):
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


# Load average function
def load_average():
	# Get load average
	load_avg = os.getloadavg()

	# Round load average to 2 decimal places
	return (round(load_avg[0], 2), round(load_avg[1], 2), round(load_avg[2], 2))


# Main function
def main():
	# Get hostname of machine
	hostname = socket.gethostname()

	# If ping not reachable
	if not ping(HOST):
		send_email(MAILGUN_API_KEY, RECIPIENTS, "[SEVERITY 1] Servers Unreachable - " + hostname, FOOTER)

	# Get load average
	load_avg = load_average()

	# Send respective email notifications if high load average
	if (load_avg[0] > 3):
		send_email(MAILGUN_API_KEY, RECIPIENTS, "[SEVERITY 2] " + hostname + " Load Average", "Load Average: " + str(load_avg) + "\n\n" + FOOTER)
	elif (load_avg[0] > 2):
		send_email(MAILGUN_API_KEY, RECIPIENTS, "[SEVERITY 3] " + hostname + " Load Average", "Load Average: " + str(load_avg) + "\n\n" + FOOTER)
	elif (load_avg[0] > 1):
		send_email(MAILGUN_API_KEY, RECIPIENTS, "[SEVERITY 4] " + hostname + " Load Average", "Load Average: " + str(load_avg) + "\n\n" + FOOTER)
	else:
		pass


# Calling of main function
if __name__ == '__main__':
	main()