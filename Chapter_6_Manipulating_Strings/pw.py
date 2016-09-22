#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'f7123ehdfjb08t948',
             'blog': '1234password',
             'luggage': '123454321'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #First argument is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
