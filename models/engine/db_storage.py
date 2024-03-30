#!/usr/bin/python3
'''
storage engine
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage:
    '''
    database storage class
    Attr:
        __engine:
        __session:
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Initializes class
        '''
        passwd = os.getenv('HBNB_MYSQL_PWD')
        user = os.getenv('HBNB_MYSQL_USER')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        url = f'mysql+mysqldb://{user}:{passwd}@{host}/{db}'
        self.__engine = create_engine(url, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData(bind=engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        '''
        returns a list of objects
        '''
        obj_list = []
        session = self.__session()
        if cls is None:
            query_res = session.query(State, City).all()
            return query_res
        else:
            query_res = session.query(cls).all()
            for obj in query_res:
                di = dict()
                key = cls.__name__ + '.' + obj.id
                di[key] = obj
                obj_list.append(di)
        return (obj_list)

    def new(self, obj):
        '''
        add obj to current session
        '''
        print(obj)
        self.__session().add(obj)

    def save(self):
        '''
        save changes to the database
        '''
        self.__session().commit()
        self.__session.remove()

    def delete(self, obj=None):
        '''
        delete obj from current session
        '''
        if obj:
            self.__session().delete(obj)

    def reload(self):
        '''
        create all database tables
        '''
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        self.__session = scoped_session(session_factory)
        session = self.__session()
        Base.metadata.create_all(self.__engine)

    def close(self):
        '''
        close current database session
        '''
        self.__session.remove()
