from sqlalchemy import Date,func
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Users(BaseModel):
    __tablename__ = 'users'
    user_id = sa.Column(sa.Integer,primary_key=True)
    user_name = sa.Column(sa.String,nullable=False)
    user_login = sa.Column(sa.String,nullable=False)
    user_password = sa.Column(sa.String,nullable=False)
    user_email = sa.Column (sa.String,nullable=False)

    def __init__(self,**args):
        super(Users,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.user_id,
            'name': self.user_name,
            'login': self.user_login,
            'email': self.user_email
        }

    def save(self,session):
        '''Funcao responsavel por salvar os dados a serem adicionados, recebendo os novos dados (self) e a sessao atual.'''     
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls,session):
        '''Funcao responsavel por retornar a listagem completa de Estoque (Stocks) do banco. Recebe respectivamente a classe de estoque (Stocks) e a sessao atual.'''
        models = []

        with session.begin():
            query = session.query(cls)
            query = query.order_by(cls.user_id)
            models = query.all()
        
        return models

    @classmethod
    def get_user_by_id(cls,session,value):
        '''Funcao responsavel por retornar responsavel por retornar os dados de um usuário individual, recebe como chave o ID (user_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(user_id=value).first()        
        return models

    @classmethod
    def get_user_by_login(cls,session,value):
        models = []
        with session.begin():
            query = session.query(cls)
            models = query.filter_by(user_login=value).first()
        return models

    @classmethod
    def delete_user(cls,session,value):
        query = session.query(cls)
        query.filter_by(user_id=value).delete()
