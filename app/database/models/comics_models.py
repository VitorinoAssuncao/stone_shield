from sqlalchemy import Date,func
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Comics(BaseModel):
    __tablename__ = 'comics'
    hq_id = sa.Column(sa.Integer,primary_key=True)
    hq_marvel_id = sa.Column(sa.Integer,nullable=True)
    hq_user_id = sa.Column(sa.Integer,nullable=False)

    def __init__(self,**args):
        super(Comics,self).__init__(**args)

    def serialize(self) -> dict:
        return {
            'id' : self.hq_id,
            'marvel_id': self.hq_marvel_id,
            'user_id': self.hq_user_id
        }

    @classmethod
    def get_list(cls,session):
        '''Funcao responsavel por retornar a listagem completa de hq's favoritadas do banco. Recebe respectivamente a classe de hq (Comics) e a sessao atual.'''
        models = []

        with session.begin():
            query = session.query(cls)
            query = query.order_by(cls.hq_id)
            models = query.all()
        
        return models

    @classmethod
    def get_hq_by_id(cls,session,value):
        '''Funcao responsavel por retornar responsavel por retornar os dados de um comic individual, recebe como chave o ID (hq_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(hq_id=value).first()        
        return models

    @classmethod
    def get_all_hqs_from_user(cls,session,value):
        '''Funcao responsavel por retornar responsavel por retornar a listagem de dados do comic de um usuário, recebe como chave o ID do usuário(user_id).'''
        models = []
        with session.begin():
            query = session.query(cls)
            models  = query.filter_by(hq_user_id=value).all()        
        return models      