from api.entities.url_entity import db, URL 

def fetch_all_urls():
    return [url.json() for url in URL.query.all()]

def add_url_to_db(hash, data):
    new_url = URL(
      id = hash,
      root_url=data['root_url'],
      child_url=data['child_url'],
      url = data['root_url'] + "/" + data['child_url'],
      shortened_url=data["root_url"] + "/" + hash
    )
    db.session.add(new_url)
    db.session.commit()

    return new_url.json()

def fetch_url_by_id(id):
    url = URL.query.filter_by(id=id).first()
    if not url:
        return None
    return url.json()