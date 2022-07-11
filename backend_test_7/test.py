import json

t1 = '{"type": "REGISTER", "user_name": "Feluk6174", "public_key": 6174, "profile_picture": "13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390", "info": "your mom is a pinnapple"}'

t2 = t1.replace('"', '\\"')

print(t2)

t3 = "{"+f'"type": "SEND", "msg": "{t2}"'+"}"

print(t3)

t4 = '{"type": "SEND", "msg": "{\\"type\\": \\"IP\\", \\"ip\\": \\"192.168.178.138:30003\\"}"}'

t5 = '{"type": "SEND", "msg": "{\\"type\\": \\"REGISTER\\", \\"user_name\\": \\"Feluk6174\\", \\"public_key\\": 6174, \\"profile_picture\\": \\"13388273892FA83BCADE910D082AB6619403DACAAA789020DC73F61839AC7390\\", \\"info\\": \\"your mom is a pinnapple\\"}"}'

j1 = json.loads(t4)
print(j1)

j2 = json.loads(t3)
print(j2)