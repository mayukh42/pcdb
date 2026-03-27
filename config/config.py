
import yaml

DEFAULT_CFG_LOCATION = "./test/resources/config.yaml"

def get_config(file=DEFAULT_CFG_LOCATION):
    try:
        with open(file, 'r') as f:
            cfg = yaml.full_load(f)
            return cfg
    except Exception as e:
        print(f"could not read yaml config at {file}")
