import logging
import pathlib

def configure_logging(FILE_NAME: str = "logfile.log") -> logging:
    logging.basicConfig(
        filename=pathlib.Path.cwd().joinpath("data", "logging", FILE_NAME), 
        encoding="utf-8", 
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s', 
        datefmt='%m/%d/%Y %H:%M:%S'
        )
    return logging