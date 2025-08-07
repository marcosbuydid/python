users = ['clari', 'marianne', 'alexa', 'aubrey', 'sophie', 'clari', 'aubrey']
logins = {}

for username in users:
    if username in logins:
        logins[username] += 1
    else:
        logins[username] = 1

for user, count in logins.items():
    print(f"{user:0}: {count} logins")
