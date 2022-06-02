import logging
import datetime
'''
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''

# It will not show any DEBUG, INFO logs
# It logs WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.WARNING)

# Method 1
logging.log(logging.DEBUG, "This is debug")
logging.log(logging.INFO, "This is info")
logging.log(logging.WARNING, "This is warning")
logging.log(logging.ERROR, "This is error")
logging.log(logging.CRITICAL, "This is critical")

# Method 2
logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")

'''
WARNING:root:This is warning
ERROR:root:This is error
CRITICAL:root:This is critical
WARNING:root:This is warning
ERROR:root:This is error
CRITICAL:root:This is critical
'''

logger = logging.getLogger("AKILAN-APP")
logger.critical("This is critical with named logger")
# CRITICAL:AKILAN-APP:This is critical with named logger

today = datetime.datetime.now()
file_name = f"{today.day:02d}-{today.month:02d}-{today.year}.log"
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


log_file_handler = logging.FileHandler(file_name)
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)

logger.critical("This is critical wiwth named logger and file")
logger.error("This is error with named logger and file")
