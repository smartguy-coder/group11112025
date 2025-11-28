from logtail import LogtailHandler
import logging
import config
import sys


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(config.LOG_LEVEL)
    logger.handlers = []

    handler = LogtailHandler(
        source_token=config.BETTERSTACK_TOKEN,
        host=config.BETTERSTACK_HOST,
    )
    logger.addHandler(handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = get_logger()
