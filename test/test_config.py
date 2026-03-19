
from config import config
import sys, json


def test_config(file):
    try:
        cfg = config.get_config(file)
        if not cfg:
            raise Exception("no config read")
        print("config", json.dumps(cfg))
        print("PASS")
    except Exception as e:
        print("FAIL", e)



if __name__ == '__main__':
    file = "./test/resources/config.yaml"
    test_config(file)

