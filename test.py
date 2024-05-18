import logging

logging_str_format = "[%(asctime)s: %(level)s: %(module)s: %(message)s %]"

logging.basicConfig(format=logging_str_format,
                    level=logging.INFO,
                    handlers=[logging.FileHandler(log_filepath)])