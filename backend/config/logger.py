import logging
import os

# Create a custom logger
logger = logging.getLogger('fastAPI')
logger.setLevel(logging.INFO)

# Create handlers
os.makedirs('/app/logs', exist_ok=True)
file_handler = logging.FileHandler('/app/logs/fastAPI.log')
stream_handler = logging.StreamHandler()  

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)