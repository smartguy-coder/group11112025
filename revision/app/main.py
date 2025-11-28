import logging

from revision import utils
from logger import logger


def main():
    utils.is_number_bigger_than_threshold(5, 8)
    utils.is_number_bigger_than_threshold(15, 8)
    utils.is_number_bigger_than_threshold(30, )
    utils.is_number_bigger_than_threshold(5, )

    logger.info('Hello here!!!')
    # logger.warning('Hello warning!!!', extra={"user": 123})
    # logger.error('Hello warning!!!', extra={"user": 123})
    logger.debug('Hello warning!!!', extra={"user": 5555})
    # logger.fatal('Hello warning!!!', extra={"user": 123})


if __name__ == "__main__":
    main()
