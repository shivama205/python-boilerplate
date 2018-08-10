import logging
import json
from decorators.general import exception_handler

log = logging.getLogger(__name__)


class JsonReader():

    @staticmethod
    @exception_handler(log)
    def read(filename):
        print('filename: ', filename)
        with open(filename, 'r') as jsonFile:
            log.info('Loading json file: {0}'.format(filename))
            return json.load(jsonFile)