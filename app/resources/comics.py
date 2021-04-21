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

    def on_post(self,req,resp,id):
        marvel_hq_id = req.media.get('marvel_id')
        user_hq_id  = id
        try:
            new_comic = Comics(hq_user_id=user_hq_id,hq_marvel_id=marvel_hq_id)
            new_comic.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possível criar o quadrinho.',
                'Validar os dados informados'
            )
            
        resp.status = falcon.HTTP_200
        resp.media = new_comic.serialize()

class ComicItem(BaseResource):
    def on_get(self,req,resp,id):
        comic_model = Comics.get_hq_by_id(self.db.session,id).serialize()
        resp.status = falcon.HTTP_200
        resp.media = comic_model

    def on_delete(self,req,resp,id):
        try:
            Comics.delete_comic(self.db.session,id)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possivel deletar o quadrinho',
                'Validar o código informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = "Quadrinho removido com sucesso"