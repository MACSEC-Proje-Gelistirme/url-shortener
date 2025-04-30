from api.repositories.url_repository import fetch_all_urls, add_url_to_db, fetch_url_by_id

def get_all_urls():
    return fetch_all_urls()

def create_url(hash, data):
    return add_url_to_db(hash, data)

def get_url_by_id(id):
    return fetch_url_by_id(id)
