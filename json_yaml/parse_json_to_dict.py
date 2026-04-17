import json

with open("task2.json", "r") as f:
    servers = json.load(f)

print(type(servers))
print(servers)
print(servers["server1"])

print()