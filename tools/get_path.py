import os

def get_file_path(config,config_base_path):
    base_path = os.path.dirname(os.path.dirname(__file__))
    #print(base_path)
    filepath = os.path.join(base_path,config,config_base_path)
    return filepath

