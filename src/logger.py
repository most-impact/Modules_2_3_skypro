import logging


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("logger.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s, %(module)s, %(levelname)s, %(message)s"))
    logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)
    return logger
