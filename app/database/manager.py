import os
import configparser
import psycopg2

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

class DBManager(object):
    def __init__(self):
        # Rota configurada para a base no docker           
        # self.connection = 'postgresql+psycopg2://dev:dev@localhost:5432/cdd_controller'
        
        # Rota Local
        # self.connection = 'postgresql+psycopg2://postgres:R@posinh@1@localhost:5432/stone_marvel'

        # Rota configurada para a base do heroku
        self.connection = 'postgresql+psycopg2://ubvmhrvfbflvlm:8d786b202b4e1e9595c90293dfda1e0c7c2ea97732b5ce61d9f4c5b92952a16d@ec2-54-162-119-125.compute-1.amazonaws.com:5432/df4lb3onq4g9r0'
        
        self.engine = sqlalchemy.create_engine(self.connection)
        self.DBSession = scoping.scoped_session(
            orm.sessionmaker(
                bind=self.engine,
                autocommit=True
            )
        )

    @property
    def session(self):
        return self.DBSession()
