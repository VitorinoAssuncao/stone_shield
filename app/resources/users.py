import falcon
import json

from app.database.models.users_models import Users 
from app.resources import BaseResource

from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash 

class UsersCollection(BaseResource):
    def on_get(self,req,resp):
        model_list = Users.get_list(self.db.session)
        obj = [user.serialize() for user in model_list]
        resp.status = falcon.HTTP_200
        resp.media = obj

    def on_post(self,req,resp):
        name_user = req.media.get('name')
        login_user = req.media.get('login')
        password_user  = generate_password_hash(req.media.get('password'))
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
        user_model = Users.get_user_by_id(self.db.session,id)
        user_model.user_name = req.media.get('name')
        user_model.user_login = req.media.get('login')
        user_model.user_password  = generate_password_hash(req.media.get('password'))
        user_model.user_email = req.media.get('email')

        try:
            user_model.save(self.db.session)

        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Atualização Não Realizada',
                'Validar valor informado.'
            )

        resp.status = falcon.HTTP_200
        resp.media = user_model.serialize()
        
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

class UserLogin(BaseResource):
    def on_post(self,req,resp):
        login  = req.media.get('login')
        password = req.media.get('password')
        try:
            user = Users.get_user_by_login(self.db.session,login)
            if user != None:
                if check_password_hash(user.user_password,password):
                    resp.status = falcon.HTTP_202
                    resp.media = user.serialize()
                else:
                    raise falcon.HTTP_BAD_REQUEST(
                        'Senha incorreta',
                        'Senha ou Login não conferem, favor tentar novamente.'
                    )
        
        except SQLAlchemyError:
            raise falcon.HTTPBadRequest(
                'Não foi possível realizar o login.',
                'Favor validar os dados informados'
            )
