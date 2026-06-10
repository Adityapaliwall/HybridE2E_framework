import yaml
import os

class ConfigReader:

    ## accessing the env.yaml file
    @staticmethod
    def read_config():
        config_path = os.path.join(os.path.dirname(__file__), 'env.yaml')

        ## reading and opening th efule
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

