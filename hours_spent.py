# Author:
#    Philip Zubel - 07 Oct 2022
# Modified:
#    Timotej Kovacka - 13 Oct 2022
# This python script returns the total hours spent on the dissertation according to the timeline
import re
import fileinput

TIMELOG_MARKDOWN = "timelog.md"
README = "README.md"

total_time = 0

with open(TIMELOG_MARKDOWN) as f:
    for line in f:
        if "hour" in line:
            obj = re.search('\d(.\d)?', line)
            if obj is not None:
                total_time += float(obj.group())

for line in fileinput.input(README, inplace=True):
    if "Time spent on dissertation -" in line:
        print("{} **{}** hours".format(line[:28], total_time))
    else:
        print(line, end="")