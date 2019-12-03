import operator
from collections import defaultdict

import parse

from utils import challenge_data
from datetime import datetime, timedelta
data = challenge_data(4)


class Data(object):
    def __init__(self, datetime, message):
        self.message = message
        self.datetime = datetime
        self.guard = None

    def __repr__(self):
        return f"{self.datetime} {self.message}"


parsed_data = []
for cycle in data.split('\n'):
    date_part = cycle[:18]
    message_part = cycle[19:]
    year,month,day,hour,minute = parse.parse('[{:d}-{:d}-{:d} {:d}:{:d}]', date_part)
    if 'asleep' in message_part or 'awake' in message_part:
        hour = 0
    parsed_data.append(
        Data(datetime(year, month, day, hour, minute), message_part))

ordered_data = sorted(parsed_data, key=lambda el: el.datetime)

guard_no = None
for data in ordered_data:
    if 'begins shift' in data.message:
        guard_no = parse.parse('Guard #{:d} begins shift', data.message)
    else:
        data.guard = int(guard_no[0])

sleepy_guard = defaultdict(timedelta)
start = None
guard_minutes = defaultdict(lambda : defaultdict(int))
for data in ordered_data:
    if 'asleep' in data.message:
        start = data.datetime
    if 'wakes up' in data.message:
        sleepy_guard[data.guard] += data.datetime - start
        for minute in range(start.minute, data.datetime.minute):
            guard_minutes[data.guard][minute] += 1
        start = None


order_sleepy = sorted(sleepy_guard.items(), key=lambda kv: kv[1], reverse=True)

print(order_sleepy[:1])

order_minutes = sorted(guard_minutes[order_sleepy[0][0]].items(), key=lambda kv: kv[1], reverse=True)

print(order_minutes[:1])


def p2():
    new = []
    for g in guard_minutes:
        for m in guard_minutes[g]:
            new.append((guard_minutes[g][m], (g, m)))
    return sorted(new, key=lambda k: k[0], reverse=True)[0]


print(p2())