# ref: https://realpython.com/python-logging/
import logging 

logging.basicConfig(
    format='%(process)d-%(levelname)s-%(message)s',
    level = logging.INFO,
)

logger = logging.getLogger('Data Engineer Project')
logger.info('teste')