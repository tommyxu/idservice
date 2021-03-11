from configprops import ConfigurationProperties


class Config(ConfigurationProperties):
    ID_SERVICE_MACHINE_ID = 0

    def __init__(self):
        super().__init__('ID_SERVICE')
        print(self.get_config_summary())


config = Config()
