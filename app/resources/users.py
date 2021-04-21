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

    def on_post(self,req,resp):
        name_user = req.media.get('name')
        login_user = req.media.get('login')
        password_user  = req.media.get('password')
        email_user = req.media.get('email')

        try:
            new_user = Users(user_name=name_user,user_login=login_user,user_password=password_user,user_email=email_user)
            new_user.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possível criar o usuário.',
                'Validar os dados informados'
            )

        resp.status = falcon.HTTP_200
        resp.media = new_user.serialize()

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
