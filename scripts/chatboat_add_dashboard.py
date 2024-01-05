from redash_manager import RedashManager

API_URL = "http://localhost:5001/api"
API_KEY = "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"

def create_visualization_and_dashboard(redash_manager, sql_query, query_name, visualization_name, dashboard_name):
    query_id = redash_manager.create_query(query_name, sql_query, 1)

    visualization_options = {
        "globalSeriesType": "line",
        "sortX": True,
        "xAxis": {"type": "-"},
        "yAxis": [{"type": "-", "name": "Views"}],
        "series": [{"name": "Views", "yAxis": 0}],
        "columnMapping": {"Date": "x", "Views": "y"},
        "defaultColumns": ["Date", "Views"]
    }
    visualization_id = redash_manager.create_visualization(visualization_name, query_id, "CHART", visualization_options)

    dashboard_slug, dashboard_id = redash_manager.create_dashboard(dashboard_name)

    widget_options = {
        "isHidden": False,
        "position": {"autoHeight": False, "sizeX": 3, "sizeY": 10, "col": 0, "row": 0}
    }
    redash_manager.add_widget_to_dashboard(dashboard_id, visualization_id, 3, widget_options)

sql_query = "SELECT * FROM total_views_by_day"  # replace this with the output from LLM
query_name = "Total Views by Day"
visualization_name = "Total Views by Day"
dashboard_name = "Total Views by Day"

redash_manager = RedashManager(API_KEY, API_URL)
create_visualization_and_dashboard(redash_manager, sql_query, query_name, visualization_name, dashboard_name)