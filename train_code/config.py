# config.py
import yaml

class Config:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r') as f:
            self.opt = yaml.safe_load(f)

    def __getattr__(self, name):
        return self.opt.get(name)
