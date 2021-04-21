from sqlalchemy import Date,func
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Characthers(BaseModel):
    __tablename__ = 'characthers'
    char_id = sa.Column(sa.Integer,primary_key=True)
    char_marvel_id = sa.Column(sa.Integer,nullable=True)
    char_user_id = sa.Column(sa.Integer,nullable=False)

    def __init__(self,**args):
        super(Comics,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.char_id,
            'marvel_id': self.char_marvel_id,
            'user_id': self.char_user_id
        }

    @classmethod
    def get_list(cls,session):
        '''Funcao responsavel por retornar a listagem completa de Personagens favoritados do banco. Recebe respectivamente a classe de Personagem (characther) e a sessao atual.'''
        models = []

        with session.begin():
            query = session.query(cls)
            query = query.order_by(cls.char_id)
            models = query.all()
        
        return models

    @classmethod
    def get_char_by_id(cls,session,value):
        '''Funcao responsavel por retornar responsavel por retornar os dados de um personagem individual, recebe como chave o ID (char_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(char_id=value).first()        
        return models

    @classmethod
    def delete_characther(cls,session,value):
        query = session.query(cls)
        query.filter_by(char_id=value).delete()

    @classmethod
    def get_all_chars_from_user(cls,session,value):
        '''Funcao responsavel por retornar responsavel  a listagem de dados de personagens de um usuário, recebe como chave o ID do usuário(user_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(char_user_id=value).all()        
        return models      