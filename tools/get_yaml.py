import yaml
from tools.get_path import *
from string import Template


def get_read(filepath):

    with open(filepath,mode='r',encoding='utf-8') as f:
        read_yml = yaml.load(stream=f,Loader=yaml.FullLoader)
        return read_yml

def get_write(filepath,data):
    with open(filepath,mode='w',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

def get_clean(filepath):
    with open(filepath,mode='w',encoding='utf-8') as f:
        f.truncate()

def get_run_data(filepath,data:dict):
    with open(filepath,mode='r',encoding='utf-8') as f:
        read_ymal = Template(f.read()).substitute(data)
        return yaml.safe_load(read_ymal)


if __name__=='__main__':
    get_data = get_write(get_file_path('page_data','test_data.yaml'),'画好')

