import requests
import json

request = requests.get("https://api.clashroyale.com/v1/players/%23999002QU/battlelog", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE3ZThhMjEyLTBkMTktNDliNS05MjExLWVlZWQ4MTAzZWNkNyIsImlhdCI6MTcyNDUwNjU3NSwic3ViIjoiZGV2ZWxvcGVyLzQzODZmOTExLTY4ZDctNmNjOS1mYzUwLTMxZGI1YzI2MmE4YiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMTMuMjQ0LjYxLjE1NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.gpKpVg6_s9_8Yb2RMfB_PHLOnHgUr__7rWX9OqK710KiB9JIpgvqcxrmvWl7dEA0f2TLJmAcPLsMshxNJGR_-g"}, params = {"limit":20})
# print(json.dumps(request.json(), indent = 2))
# Define the filename
filename = "data.json"

# Write the JSON data to a file
with open(filename, 'w') as json_file:
    json.dump(request.json(), json_file, indent=2)

print(f"JSON data has been saved to {filename}")