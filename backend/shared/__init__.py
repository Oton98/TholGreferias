import logging

# Configura el logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
