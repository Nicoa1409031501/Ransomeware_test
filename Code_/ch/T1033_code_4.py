logon_events = get_logon_events()
parsed_events = parse_logon_events(logon_events)

print("Logon Events:")
for event in parsed_events:
    print(event)