import mysql.connector
from config.settings import DB_CONFIG

class DatabaseConnection:
    '''
    Responsible only for e creating MySQL connections
    '''

    @staticmethod
    def get_connection():
        return mysql.connector.connect(**DB_CONFIG)