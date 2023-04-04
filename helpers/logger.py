# ref: https://realpython.com/python-logging/
import logging 

logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s',
    level=logging.INFO,
    force=True
)

logger = logging.getLogger('Data Engineer Project')
logger.info('teste')