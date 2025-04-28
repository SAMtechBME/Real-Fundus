# config.py
import yaml

class Config:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r') as f:
            cfg_dict = yaml.safe_load(f)
        
        for k, v in cfg_dict.items():
            setattr(self, k, DictToObject(v))

class DictToObject:
    def __init__(self, dict_):
        for k, v in dict_.items():
            if isinstance(v, dict):
                setattr(self, k, DictToObject(v))
            else:
                setattr(self, k, v)

