import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/bb23ue")

print(post_codes_req)
print(f"Status code: {post_codes_req.status_code}")
print(f"Headers: {post_codes_req.headers}")
print(f"Content: {post_codes_req.content}")
print(f"JSON: {post_codes_req.json()}")
print(f"Data type of JSON: {type(post_codes_req.json())}")
print()
print(f"Region: {post_codes_req.json()["result"]["region"]}")