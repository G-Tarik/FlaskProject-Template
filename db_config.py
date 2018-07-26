class PGSQL:
    USER = 'dbuser'
    PASS = 'pass'
    DB_NAME = 'flask_db'
    HOST = 'localhost'
    PORT = '5432'
    URI = f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}'
