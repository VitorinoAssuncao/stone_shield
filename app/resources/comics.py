import falcon
import json

from app.database.models.comics_models import Comics 
from app.resources import BaseResource

from sqlalchemy.exc import IntegrityError,SQLAlchemyError

class ComicsCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Comics.get_list(self.db.session)
        obj = [comic.serialize() for comic in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj

class ComicsUserCollection(BaseResource):
    def on_get(self,req,resp,id):
        model_list = Comics.get_all_hqs_from_user(self.db.session,id)
        obj = [comic.serialize() for comic in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj

class ComicItem(BaseResource):
    def on_get(self,req,resp,id):
        comic_model = Comics.get_hq_by_id(self.db.session,id).serialize()
        resp.status = falcon.HTTP_200
        resp.media = comic_model