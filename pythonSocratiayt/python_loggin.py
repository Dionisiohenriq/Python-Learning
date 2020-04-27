import logging

# Create and configure Logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\menuu\Documents\\python\\pythonSocratiayt\\teste.log", level=logging.DEBUG,
     format=LOG_FORMAT,
     filemode='w')

logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")