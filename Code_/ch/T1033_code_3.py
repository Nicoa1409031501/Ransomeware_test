import win32evtlog

def get_logon_events():
    events = []
    hand = win32evtlog.OpenEventLog(None, "System")
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    events = []
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        
        for event in events:
            if event.EventID == win32evtlog.EvtLogon:
                events.append(event)
    
    win32evtlog.CloseEventLog(hand)
    return events

def parse_logon_events(events):
    logon_events = []
    for event in events:
        logon_events.append(event.StringInserts[0])
    return logon_events