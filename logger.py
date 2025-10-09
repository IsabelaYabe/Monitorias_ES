import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s | %(levelname)s | %(module)s : %(funcName)s : line %(lineno)d - %(message)s"
    )