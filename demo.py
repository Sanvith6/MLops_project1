# demo.py
import logging

# Suppress PyMongo debug logs
logging.getLogger("pymongo").setLevel(logging.WARNING)

from pymongo import MongoClient

client = MongoClient("your_connection_string")
db = client["Proj1"]

from from_root import from_root
from src.logger import logging  # <- Just importing logging triggers setup

print(f"Root path: {from_root()}")

logging.debug("This is a debug message.")
#logging.info("This is an info message.")
#logging.warning("This is a warning message.")
#logging.error("This is an error message.")
#logging.critical("This is a critical message.")



from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()
