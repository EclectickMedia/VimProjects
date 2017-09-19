import logging
import logging.handlers as handlers

from os import path
PROGRAM_PATH = path.split(path.realpath(__file__))[0]
SEARCHER_LOG_PATH = path.join(PROGRAM_PATH, 'logs', 'logger')

# BEGIN Logger setup
file_formatter = logging.Formatter(
    '%(asctime)s:'
    '%(filename)-24s:'
    '%(name)-24s:'
    '%(levelname)-10s:'
    '%(funcName)-24s:'
    '%(lineno)-4d:'
    '%(message)s'
)

stream_formatter = logging.Formatter(
    '%(levelname)-10s:'
    '%(name)-20s:'
    '%(message)s'
)

file_handler = handlers.RotatingFileHandler(SEARCHER_LOG_PATH,
                                            maxBytes=500000, backupCount=5)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)
stream_handler.setLevel(logging.INFO)

base_logger = logging.getLogger('base')
base_logger.setLevel(logging.DEBUG)
base_logger.addHandler(file_handler)
base_logger.addHandler(stream_handler)

parser_logger = logging.getLogger('base.parser')
