import logging
import os
from datetime import datetime

LOG_FILE = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO,
    force=True
)

def log_exception(exc_info):
    """
    Log an exception with its traceback
    Args:
        exc_info: Exception information from sys.exc_info()
    """
    logging.error("Exception occurred", exc_info=exc_info)

if __name__ == "__main__":
    logging.info("Logger has been set up.")
    try:
        # Test exception logging
        raise ValueError("Test exception")
    except Exception as e:
        log_exception(exc_info=True)