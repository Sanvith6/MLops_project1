# demo.py

from from_root import from_root
from src.logger import logging  # <- Just importing logging triggers setup

print(f"Root path: {from_root()}")

logging.debug("This is a debug message.")
#logging.info("This is an info message.")
#logging.warning("This is a warning message.")
#logging.error("This is an error message.")
#logging.critical("This is a critical message.")



# # below code is to check the exception config
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
#     raise MyException(e, sys) from e

