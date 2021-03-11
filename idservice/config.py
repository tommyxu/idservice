from configprops import ConfigurationProperties
import secrets


class Config(ConfigurationProperties):
    ID_SERVICE_MACHINE_ID = -1

    def __init__(self):
        super().__init__('ID_SERVICE')
        if self.ID_SERVICE_MACHINE_ID < 0:
            self.ID_SERVICE_MACHINE_ID = secrets.randbits(8)
        print(self.get_config_summary())


config = Config()
