import falcon
import json

from app.database.models.characthers_models import  Characthers
from app.resources import BaseResource

from sqlalchemy.exc import IntegrityError,SQLAlchemyError

class CharacthersCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Characthers.get_list(self.db.session)
        obj = [char.serialize() for char in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj

class CharacthersUserCollection(BaseResource):
    def on_get(self,req,resp,id):
        model_list = Characthers.get_all_chars_from_user(self.db.session,id)
        obj = [char.serialize() for char in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj

    def on_post(self,req,resp,id):
        marvel_char_id = req.media.get('marvel_id')
        user_char_id  = id
        try:
            new_char = Characthers(char_user_id=user_char_id,char_marvel_id=marvel_char_id)
            new_char.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possível criar o quadrinho.',
                'Validar os dados informados'
            )
            
        resp.status = falcon.HTTP_200
        resp.media = new_char.serialize()


class CharactherItem(BaseResource):
    def on_get(self,req,resp,id):
        char_model = Characthers.get_char_by_id(self.db.session,id).serialize()
        resp.status = falcon.HTTP_200
        resp.media = char_model

    def on_delete(self,req,resp,id):
        try:
            Characthers.delete_characther(self.db.session,id)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possivel deletar o personagem',
                'Validar o código informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = "Personagem removido com sucesso"