from urllib import unquote
from datetime import datetime

import re

FMT = '%H:%M:%S'

def calc_timedelta(t1, t2):
    t1, t2 = map(lambda x: datetime.strptime(x, FMT), [t1, t2])

    return (t2 - t1).total_seconds()

def parse_payload(text):
    text = unquote(text)
    rule = re.compile(r"\),(\d+),1\).*'([\w}{])'")
    return rule.findall(text)


timestamp = open('timestamp').read().split('\n')[:-1]
time_delta = [
    calc_timedelta(timestamp[x], timestamp[x+1]) \
        for x in range(0, len(timestamp) - 1)
]

time_delta = [time_delta[0]] + time_delta

payload = open('payload').read().split('\n')[:-1]
parsed_payload = map(parse_payload, payload)

result = dict()
for p,t in zip(parsed_payload, time_delta):
    if t > 2:
        order, val = p[0]
        result[int(order)] = val

print ''.join(result.values())
