import mysql.connector
from Config.settings import DB_CONFIG


class DatabaseConnection:
    '''
    Responsible only for creating MySQL connections
    '''

    @staticmethod
    def get_connection():
        return mysql.connector.connect(**DB_CONFIG)