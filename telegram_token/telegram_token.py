import logging

import configuration.file_settings_locator
import yaml

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
log_file = configuration.file_settings_locator.get_file_from_working_directory("log")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class TelegramToken:
    _secret = ""

    def __init__(self, secret: str = ""):
        if secret:
            self._secret = secret
        else:
            self._secret = self.read_from_config_file()

    @staticmethod
    def read_from_config_file() -> str:
        secret_location = configuration.file_settings_locator.get_file_from_working_directory("config.yaml")
        try:
            with open(secret_location, "r") as config_file:
                configs = yaml.safe_load(config_file)
                return configs["token_bot"]
        except IOError:
            logger.debug(f"Could not read configuration file in '{secret_location}'"
                         f"{IOError.strerror}")

    def write_to_config_file(self) -> None:
        secret_location = configuration.file_settings_locator.get_file_from_working_directory("config.yaml")
        configs = {"token_bot": self.get_secret()}
        with open(secret_location, "w") as config_file:
            config_file.write(yaml.safe_dump(configs))

    def get_secret(self) -> str:
        return self._secret

    def set_secret(self, secret):
        self._secret = secret
