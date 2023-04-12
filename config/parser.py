# register your model in this script
# import the model class
model_map = {}

trainer_map = {}

import os
from pathlib import Path
import json
import yaml
import pickle
import numpy as np

def model_config_reader(config_file_name):
    # return a dict configuration
    model_config = None
    if isinstance(config_file_name, dict):
        model_config =  config_file_name

    path = Path(os.path.join('config_files', config_file_name))
    if path.suffix == ".json":
        model_config =  json.load(open(path, "r"))
    elif path.suffix in [".yaml", ".yml"]:
        model_config =  yaml.load(open(path, "r"), Loader=yaml.FullLoader)
    elif path.suffix in [".pkl", ".pickle"]:
        model_config =  pickle.load(open(path, "rb"))
    else:
        raise ValueError("Only JSON, YaML and pickle files supported.")

    model_config['model_class'] = model_map[model_config['model']]
    model_config['trainer_class'] = trainer_map[model_config['trainer']]

    return model_config