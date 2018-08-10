import logging.config
import logging

from containers.application_container import Application
from containers.core_container import Configs
from file_readers.json_reader import JsonReader

logging.config.dictConfig(JsonReader.read('configs/logging.json'))
log = logging.getLogger(__name__)

if __name__ == "__main__":
    # Configs.config.override({})
    Application.main()
