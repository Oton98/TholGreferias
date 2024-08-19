import os

class Config:
    # MySQL Database Configuration
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_USER = os.getenv('MYSQL_USER', 'thol_thol')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Thol/97531')
    MYSQL_DB = os.getenv('MYSQL_DB', 'thol_thol')
    # MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    # MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'firewall15')
    # MYSQL_DB = os.getenv('MYSQL_DB', 'thol')
    MYSQL_CONNECT_TIMEOUT = int(os.getenv('MYSQL_CONNECT_TIMEOUT', 10))

    # Additional MySQL Configuration for Reliability and Performance
    MYSQL_AUTOCOMMIT = bool(os.getenv('MYSQL_AUTOCOMMIT', True))
    MYSQL_USE_UNICODE = True
    MYSQL_CHARSET = 'utf8mb4'
    MYSQL_CURSORCLASS = 'DictCursor'
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()