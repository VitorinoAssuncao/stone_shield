import falcon

from app.database.manager import DBManager
from app.resources.users import UsersCollection, UsersItem
from app.resources.comics import ComicsCollection, ComicsUserCollection,ComicItem
from app.middleware import HandleCORS

api = falcon.API(middleware=[HandleCORS()])
db = DBManager()

users = UsersCollection(db)
user = UsersItem(db)

comics = ComicsCollection(db)
user_comics = ComicsUserCollection(db)
comic = ComicItem(db)

api.add_route('/users',users)
api.add_route('/users/{id}',user)
api.add_route('/comics',comics)
api.add_route('/comics/{id}',comic)
api.add_route('/users/{id}/comics',user_comics)

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1",5000,api)
    httpd.serve_forever()