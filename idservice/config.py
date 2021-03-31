from configprops import ConfigurationProperties
import secrets


class Config(ConfigurationProperties):
    ID_SERVICE_SNOWFLAKE_MACHINE_ID: int = secrets.randbits(10)

    def __init__(self):
        super().__init__("ID_SERVICE", debug=True)
        # print(self.get_config_summary())


config = Config()
