import logging
import pathlib

FILE_NAME = "logfile.log"

logging.basicConfig(
    filename=pathlib.Path.cwd().joinpath("data", "logging", FILE_NAME), 
    encoding="utf-8", 
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S'
    )
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

def configure_logging() -> logging:
    logging.basicConfig(
        filename=pathlib.Path.cwd().joinpath("data", "logging", FILE_NAME), 
        encoding="utf-8", 
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(message)s', 
        datefmt='%m/%d/%Y %H:%M:%S'
        )
    return logging