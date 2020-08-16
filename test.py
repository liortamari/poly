input_data = [
    {"name": "device", "strVal": "iPhone", "metadata": "not interesting"},
    {"name": "isAuthorized", "boolVal": "false", "lastSeen": "not interesting"}
]

output = {
    item["name"]: item[val]
    for item in input_data
    for val in item if val.endswith("Val")
}
print(output)
