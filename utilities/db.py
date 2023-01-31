from typing import Optional, Dict, Any
from sqlalchemy import create_engine, Engine, text
from sqlalchemy.exc import OperationalError

class DB:

    def generate_connection_uri(
        self,
        db_engine: str,
        db_host: str,
        db_port: str,
        db_user: str,
        db_pass: str,
        db_name: str,
    ) -> str:

        return f'{db_engine}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


    def create_engine(
        self,
        connection_uri: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Engine:
        if params and type(params) == dict:
            pass
        else:
            params = {}

        return create_engine(
            connection_uri, 
            **params
        )
    
    def create_db(
        self,
        existing_db_connection_uri: str,
        new_db_connection_uri: str,
    ):
        try:
            engine = self.create_engine(
                new_db_connection_uri
            )
            db_name = engine.url.database
            conn = engine.connect()
            conn.close()
            raise Exception(f'database {db_name} already exists')
        except OperationalError as oe:
            if 'does not exist' in oe.__str__():
                engine = self.create_engine(
                    existing_db_connection_uri
                )
                conn = engine.connect()
                conn.execution_options(isolation_level="AUTOCOMMIT").execute(text(f'create database {db_name}'))
                conn.close()
            else:
                raise oe
