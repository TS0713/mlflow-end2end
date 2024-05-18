import os 
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # Message format of the log
# asctime => ascii time 
# levelname => type of log [INFO,ERROR,WARNING]
# module => file name
# message => message from the logger function

log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath), # file handler creates log folder and inside it will place/write all the logs to .log file
        logging.StreamHandler(sys.stdout) # strea,handler will just print the log in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")