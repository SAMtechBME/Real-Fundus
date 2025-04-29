# config.py
import yaml
class DictToObject:
    def __init__(self, dict_):
        for k, v in dict_.items():
            if isinstance(v, dict):
                setattr(self, k, DictToObject(v))
            else:
                setattr(self, k, v)

class Config:
    def __init__(self, yaml_file):
        import yaml
        with open(yaml_file, 'r') as f:
            config_dict = yaml.safe_load(f)

        for k, v in config_dict.items():
            if isinstance(v, dict):
                setattr(self, k, DictToObject(v))
            else:
                setattr(self, k, v)


