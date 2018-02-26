import tailer
from directkeys import PressKey, ReleaseKey, One, Two, Three, Four, Five, Six
import time, sys, re

# usage : python autocleric.py CHARACTER_NAME

charname = sys.argv[1]
logname = "C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest\Logs\eqlog_"+charname+"_agnarr.txt"
# filters.key is the Key to send, filters.value is the regex
filters = {
"Five":"Amudar.*Now$",
"Six":"KEI ME"
}
# direct input key mappings
keys = {
'One': 0x02,
'Two': 0x03,
'Three': 0x04,
'Four': 0x05,
'Five': 0x06,
'Six': 0x07
}
regexes = []
for k,v in filters.items():
    v = re.compile(v)
    filters[k] = v

for line in tailer.follow(open(logname)):
    print line
    for k,v in filters.items():
        if re.search(v, line):
            PressKey(keys[k])
            time.sleep(0.35)
            ReleaseKey(keys[k])
