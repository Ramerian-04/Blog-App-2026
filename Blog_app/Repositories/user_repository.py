from DB.connection import DatabaseConnection


class UserRepository:
    def user_exists(self,user_id):
        connection=None
        cursor=None
        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor()
            cursor.execute(
                "SELECT user_id FROM users WHERE user_id=%s;",
                (user_id,)
            )
            return cursor.fetchone() is not None
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def create_user(self,user):
        connection=None
        cursor=None
        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor()
            query='''
            INSERT INTO users(user_id, password, first_name, last_name)
            VALUES(%s,%s,%s,%s);
            '''
            cursor.execute(query,(user.user_id,user.password,user.first_name,user.last_name))
            connection.commit()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def find_user(self,user_id,password):
        connection=None
        cursor=None

        try:
            connection=DatabaseConnection.get_connection()
            cursor=connection.cursor(dictionary=True)
            cursor.execute(
                '''
                SELECT user_id, password, first_name, last_name
                FROM users 
                WHERE user_id=%s AND password=%s
                ''',
                (user_id,password)

            )
            return cursor.fetchone()
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()