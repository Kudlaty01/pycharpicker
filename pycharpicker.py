#!/usr/bin/env python3
import re, getpass, subprocess
pwd = getpass.getpass(prompt='Password? ')
xdt = 'xdotool'
get_win = 'getactivewindow'
clearmods = '--clearmodifiers'
indexes = input("pick your chars:\n")
output = ''
for index in re.findall(r'\d+', indexes):
    output += pwd[int(index)-1]
params=[
        [get_win, 'windowclose'],
        ['type', clearmods, '--', output],
        [get_win, 'windowfocus'],
        ['key', clearmods, 'Return']
        ]
for p in params:
    subprocess.run([xdt] + p)
