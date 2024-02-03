import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql

class User:
    params = {
        "user": "postgres",
        "password": "hack4soc",
        "host": "localhost",
        "port": "5432"
    }

    @classmethod
    def open_connection(cls, dbname='postgres'):
        try:
            cls.params["dbname"] = dbname
            cls.conn = psycopg2.connect(**cls.params)
            cls.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cls.cur = cls.conn.cursor()
            print('Connection Established')
        except psycopg2.Error as e:
            print(f"Error opening connection: {e}")

    @classmethod
    def create_database(cls, dbname='users'):
        cls.open_connection()  # Ensure connection is open

        try:
            cls.cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), (dbname,))
            if not cls.cur.fetchone():
                cls.cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
            cls.conn.close()  # Close the previous connection before switching databases
            
            cls.open_connection(dbname)  # Reopen connection with the new database
        except psycopg2.Error as e:
            print(f"Error creating database: {e}")

    @classmethod
    def create_table(cls):
        cls.open_connection()  
        try:
            cls.cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100),
                    phone INT,
                    password VARCHAR(100),
                    date TIMESTAMP
                )
            """)
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")

    @classmethod
    def insert_user(cls, name, email, phone, password, registration_date):
        cls.open_connection()  
        try:
            query = """
                INSERT INTO users (name, email, phone, password, date) VALUES (%s, %s, %s, %s, %s)
            """
            cls.cur.execute(query, (name, email, phone, password, registration_date))
        except psycopg2.Error as e:
            print(f"Error inserting user: {e}")
    
    
    @classmethod
    def search(cls,name,password):

        cls.open_connection() 
        cls.cur.execute("SELECT * FROM USERS WHERE name = %s AND password = %s", (name, password))


        user_data = cls.cur.fetchone()
        return user_data

        

    @classmethod
    def fetch_data(cls):
        cls.open_connection()  
        try:
            cls.cur.execute("SELECT * FROM users")
            return cls.cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error fetching data: {e}")
            return None

    @classmethod
    def close_connection(cls):
        try:
            if cls.cur is not None:
                cls.cur.close()
            if cls.conn is not None:
                cls.conn.close()
            print('Connection closed')
        except psycopg2.Error as e:
            print(f"Error closing connection: {e}")
