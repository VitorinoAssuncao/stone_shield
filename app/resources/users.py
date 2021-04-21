import falcon
import json

from app.database.models.users_models import Users 
from app.resources import BaseResource

from sqlalchemy.exc import IntegrityError,SQLAlchemyError

class UsersCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Users.get_list(self.db.session)
        obj = [user.serialize() for user in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj


class UsersItem(BaseResource):
    def on_get(self,req,resp,id):
        user_model = Users.get_user_by_id(self.db.session,id).serialize()
        resp.status = falcon.HTTP_200
        resp.media = user_model
        
    def on_put(self,req,resp,id):
        user_model = User.get_user_by_id(self.db.session,id)
        user_model.stock_value = req.media.get('value')
        
        try:
            user_model.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Atualização Não Realizada',
                'Validar valor informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = stock_model.serialize()

    def on_delete(self,req,resp,id):
        try:
            Users.delete_user(self.db.session,id)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possivel deletar o usuário',
                'Validar o código informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = "Usuário deletado com sucesso"
