import tailer
from directkeys import PressKey, ReleaseKey, Five
import time

charname = "Amudar"

for line in tailer.follow(open("C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest\Logs\eqlog_Kieffers_agnarr.txt")):
    if charname in line and ("Now" in line or "now" in line):
        PressKey(Five)
        time.sleep(0.35)
        ReleaseKey(Five)
        print line
