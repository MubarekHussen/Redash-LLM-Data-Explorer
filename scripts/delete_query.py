import requests

api_key = "GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"
redash_url = "http://localhost:5001"

api_url = f"{redash_url}/api/queries"
headers = {"Authorization": f"Key {api_key}"}
response = requests.get(api_url, headers=headers)
queries = response.json()["results"]

for query in queries:
    query_id = query["id"]
    api_url = f"{redash_url}/api/queries/{query_id}"
    response = requests.delete(api_url, headers=headers)