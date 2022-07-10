import json

t = '{"type": "hello"}'

j = json.loads(t)

print("t", t, type(t))

print("j", j, type(j))
