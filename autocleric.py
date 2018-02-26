import tailer
from directkeys import PressKey, ReleaseKey, Five
import time

# usage : python autocleric.py CHARACTER_NAME

charname = sys.argv[0]
logname = "C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest\Logs\eqlog_"+charname+"_agnarr.txt"

for line in tailer.follow(open(logname)):
    if charname in line and ("Now" in line or "now" in line):
        PressKey(Five)
        time.sleep(0.35)
        ReleaseKey(Five)
        print line
