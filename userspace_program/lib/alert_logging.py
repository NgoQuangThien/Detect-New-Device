import os
import zlib
import logging
import logging.handlers
from logging import Formatter


# name the compressed file
def namer(name):
    return name + ".gz"

# read the data from source, compress it, write it to dest and delete source
def rotator(source, dest):
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, "wb") as df:
            df.write(compressed)
    os.remove(source)

def create_time_based_rotating_log(log_path):
    """"""

    # Checks if the path exists otherwise tries to create it
    if not os.path.exists(log_path):
        try:
            os.makedirs(log_path)
        except Exception:
            exc_type, exc_value, exc_traceback = os.sysconf_names.exc_info()
            print(exc_type, exc_value, exc_traceback)

    # Sets the format and level of logging records
    format = '%(message)s'
    level=logging.CRITICAL

    # Does basic configuration for the logging system
    logging.basicConfig(format=format, level=level)

    # Instantiates a logger object
    logger = logging.getLogger("Rotating Log")
 
    # Creates at most 30 backup files
    handler = logging.handlers.TimedRotatingFileHandler(filename=''.join([log_path, 'alert.log']),
                                       when="d",
                                       interval=1,
                                       backupCount=30)
    formatter = Formatter(format)
    handler.setFormatter(formatter)
    handler.rotator = rotator
    handler.namer = namer
    logger.addHandler(handler)
