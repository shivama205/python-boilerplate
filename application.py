import logging
from decorators.general import exception_handler

log = logging.getLogger(__name__)


@exception_handler(log)
def main():
    log.info('Starting main application')


