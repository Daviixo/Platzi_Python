
# apikey = 'MDg3NDQzNzkzNjA2OqxyZbV8AvfKBwL73rrJmX6/qln6'

# import the installed Jira library
from jira import JIRA
  
# Specify a server key. It is your  domain 
# name link.
jiraOptions = {'server': "https://jira.ops.expertcity.com"}
  
# Get a JIRA client instance, Pass 
# Authentication parameters
# and  Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options = jiraOptions, 
            basic_auth = ("ddiaz",
                          "MDg3NDQzNzkzNjA2OqxyZbV8AvfKBwL73rrJmX6/qln6"))
  
# While fetching details of a single issue,
# pass its UniqueID or Key.
singleIssue = jira.issue('TSD-451057')
print('{}: {}:{}'.format(singleIssue.key,
                         singleIssue.fields.summary,
                         singleIssue.fields.reporter.displayName))