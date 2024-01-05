import requests


class RedashManager:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {"Authorization": self.api_key}

    def create_query(self, name, query, data_source_id):
        data = {
            "name": name,
            "query": query,
            "data_source_id": data_source_id,
        }
        response = requests.post(f"{self.api_url}/queries", headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()["id"]
        else:
            return None

    def create_visualization(self, name, query_id, type, options):
        data = {
            "name": name,
            "query_id": query_id,
            "type": type,
            "options": options,
        }
        response = requests.post(f"{self.api_url}/visualizations", headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()["id"]
        else:
            return None

    def create_dashboard(self, name):
        data = {"name": name}
        response = requests.post(f"{self.api_url}/dashboards", headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()["slug"], response.json()["id"]
        else:
            return None, None

    def add_widget_to_dashboard(self, dashboard_id, visualization_id, width, options):
        data = {
            "visualization_id": visualization_id,
            "dashboard_id": dashboard_id,
            "width": width,
            "options": options,
        }
        response = requests.post(f"{self.api_url}/dashboards/{dashboard_id}", headers=self.headers, json=data)
        if response.status_code == 200:
            return True
        else:
            return False