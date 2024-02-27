from redash_manager import RedashManager
from redash.handlers.chat import ChatResource

API_URL = "http://localhost:5001/api"
API_KEY = "Key GDsHJa3r8nRgo9vcxoAd47zXxPt8zCuZJehRanVg"


def create_query(redash_manager, sql_query, query_name):
    query_id = redash_manager.create_query(query_name, sql_query, 1)
    return query_id


sql_query = ""
query_name = "Total Views by Day"

redash_manager = RedashManager(API_KEY, API_URL)
query_id = create_query(redash_manager, sql_query, query_name)

print(f"Created query with ID: {query_id}")