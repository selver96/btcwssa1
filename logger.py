import logging

LOG_FILE_NAME = "logfile"

def basic_config():
    logging.basicConfig(
        filename=LOG_FILE_NAME+".txt",
        format="%(asctime)s - %(levelname)s - %(message)s ",
        filemode="w",
        level=logging.DEBUG)


def get_logger():
    basic_config()
    return logging.getLogger()
