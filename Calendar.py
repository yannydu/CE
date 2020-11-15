#from pprint import pprint
from Google import Create_Service, add_event, delete_event

#Initializtion for Google Calendar
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# request_body = {
#     'summary': 'Assignments'
# }
#
# response = service.calendars().insert(body=request_body).execute()


"""
Create an event
"""
#add_event(service)


# Delete an event
#delete_event(service)