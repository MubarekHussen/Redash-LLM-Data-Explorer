import requests

api_url = "http://localhost:5001/api/queries"
headers = {"Authorization": "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"}

query_data = {
    "name": "Your Query",
    "query": "SELECT * FROM total_views_by_day",
    "data_source_id": 1,
}

response = requests.post(api_url, headers=headers, json=query_data)
query_id = response.json()["id"]

api_url = "http://localhost:5001/api/visualizations"
headers = {"Authorization": "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"}

visualization_data = {
    "name": "Your Visualization",
    "query_id": query_id,
    "type": "CHART",
    "options": {
        "globalSeriesType": "line",
        "sortX": True,
        "xAxis": {"type": "-"},
        "yAxis": [{"type": "-", "name": "Views"}],
        "series": [{"name": "Views", "yAxis": 0}],
        "columnMapping": {"Date": "x", "Views": "y"},
        "defaultColumns": ["Date", "Views"]
    },
}

response = requests.post(api_url, headers=headers, json=visualization_data)
if response.status_code == 200:
    visualization_id = response.json()["id"]
    print(f"Visualization created successfully. Visualization ID: {visualization_id}")
else:
    print(f"Failed to create visualization. Status code: {response.status_code}")
    print(response.text)

# api_url = "http://localhost:5001/api/dashboards"
# headers = {"Authorization": "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"}

# dashboard_data = {
#     "name": "Your Dashboard",
# }

# response = requests.post(api_url, headers=headers, json=dashboard_data)
# dashboard_id = response.json()["id"]
# dashboard_slug = response.json()["slug"]
# print(f"Dashboard created successfully. Dashboard slug: {dashboard_slug}")

# api_url = f"http://localhost:5001/api/dashboards/{dashboard_slug}/widgets"
# headers = {"Authorization": "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"}

# widget_data = {
#     "visualization_id": visualization_id,
#     "dashboard_id": dashboard_id,
#     "width": 3,
#     "options": {
#         "isHidden": False,
#         "position": {"autoHeight": False, "sizeX": 3, "sizeY": 10, "col": 0, "row": 0}
#     },
# }

# response = requests.post(api_url, headers=headers, json=widget_data)
# if response.status_code == 200:
#     print("Widget created successfully.")
#     print(response.json())
# else:
#     print(f"Failed to create widget. Status code: {response.status_code}")
#     print(response.text)