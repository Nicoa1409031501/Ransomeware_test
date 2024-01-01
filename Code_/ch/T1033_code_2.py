current_user = get_current_user()
logged_in_users = get_logged_in_users()
process_owners = get_process_owners()

print("Current User:", current_user)
print("Logged In Users:", logged_in_users)
print("Process Owners:")
for username, processes in process_owners.items():
    print(username, ":", processes)