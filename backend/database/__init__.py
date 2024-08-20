import pymysql as MySQLdb
from backend.config import Config
from backend.shared import logger

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.logger = logger
        
    def connect(self):
        if not self.connection or not self.connection.open:
            self.logger.info("Establishing new database connection...")
            try:
                self.connection = MySQLdb.connect(
                    host=Config.MYSQL_HOST,
                    user=Config.MYSQL_USER,
                    passwd=Config.MYSQL_PASSWORD,
                    db=Config.MYSQL_DB,
                    port=Config.MYSQL_PORT,
                    connect_timeout=Config.MYSQL_CONNECT_TIMEOUT,
                    autocommit=Config.MYSQL_AUTOCOMMIT,
                    cursorclass=MySQLdb.cursors.DictCursor
                )
                self.logger.info("Database connection established successfully.")
            except MySQLdb.MySQLError as e:
                self.logger.error(f"Error connecting to database: {e}")
                raise e
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.logger.info("Database connection closed.")