from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class __DbConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = f"{"sqlite"}:///{"storage.db"}"

        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)  # create a session based on connection with database
        return self  # statement return self serves to return all actions executed on method.

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = __DbConnectionHandler()
