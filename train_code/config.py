import yaml

class DictToObject:
    def __init__(self, dict_):
        if not isinstance(dict_, dict):
            raise ValueError(f"Expected dict, got {type(dict_)}")

        for k, v in dict_.items():
            if isinstance(v, dict):
                setattr(self, k, DictToObject(v))
            elif isinstance(v, list):
                # Recursively convert list of dicts
                setattr(self, k, [DictToObject(i) if isinstance(i, dict) else i for i in v])
            else:
                setattr(self, k, v)

class Config:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r') as f:
            config_dict = yaml.safe_load(f)

        for k, v in config_dict.items():
            if isinstance(v, dict):
                setattr(self, k, DictToObject(v))
            elif isinstance(v, list):
                setattr(self, k, [DictToObject(i) if isinstance(i, dict) else i for i in v])
            else:
                setattr(self, k, v)
