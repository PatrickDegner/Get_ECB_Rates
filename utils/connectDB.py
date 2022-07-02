import psycopg2
import utils.const


class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(database=f'{utils.const.database}', user=f'{utils.const.user}', password=f'{utils.const.password}', host=utils.const.host, port=utils.const.port)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()