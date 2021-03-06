# required imports
from jira import JIRA
from jira import JIRAError
import getpass
import sys

# Attempts a connection to the specified jira server with the username and password. If
def login():
	print 'What is your Atlassian login? e.g. harry.bassettbutt@gohubble.com: '
	username = raw_input()
	# password is entered securely
	password = getpass.getpass(prompt='What is your password? : ')
	# sets up the server to connect to
	jiraOptions = {'server': 'https://insightsoftware.atlassian.net'}
	jira = None
	try:
		# uses the basic authentication to login to the jira server and return a jira object
		jira = JIRA(options=jiraOptions, basic_auth=(username, password))
	except Exception,e:
		print 'Login error - check your credentials'	
	return jira
	
