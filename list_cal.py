from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def get_calendar_list():
    service = get_calendar_service()
    # Call the Calendar API
    print('Getting list of calendars')
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])

    if not calendars:
        print('No calendars found.')
    for calendar in calendars:
        summary = calendar['summary']
        id = calendar['id']
        primary = "Primary" if calendar.get('primary') else ""
        print("%s\t%s\t%s" % (summary, id, primary))


def get_events_list():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting List o 10 events')
    events_result = service.events().list(
        calendarId='family13154378497060548131@group.calendar.google.com', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], event['id'])


def create_new_event(dt, summary, description):
    service = get_calendar_service()

    start = dt.isoformat()
    end = (dt + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(
        calendarId='ablyashev.artur@gmail.com',
        body={
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": start,
                "timeZone": 'Asia/Yekaterinburg'
            },
            "end": {
                "dateTime": end,
                "timeZone": 'Asia/Yekaterinburg'
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 1440},
                ],
            },
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


if __name__ == '__main__':
    # get_calendar_list()
    # get_events_list()
    d = datetime.now().date()
    create_new_event(datetime(d.year, d.month, d.day, 0), 'Test summary', 'Test description')
