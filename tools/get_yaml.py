import os
import yaml
from tools.get_path import *
from string import Template
import page

def get_read(filepath):

    with open(filepath,mode='r',encoding='utf-8') as f:
        read_ymal = yaml.load(stream=f,Loader=yaml.FullLoader)
        return read_ymal

def get_write(filepath,data):
    with open(filepath,mode='a',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

def get_clean(filepath):
    with open(filepath,mode='w',encoding='utf-8') as f:
        f.truncate()

def get_run_data(filepath,data:dict):
    with open(filepath,mode='r',encoding='utf-8') as f:
        read_ymal = Template(f.read()).substitute(data)
        return yaml.safe_load(read_ymal)


if __name__=='__main__':
    get_data = get_read(get_file_path('page_data','page_data_mail_pwd_login.yaml'))
    print(get_data)
    a = get_data[0]["loggin_change_password"]
    print(a)
    print(type(a))
    a = eval(a)
    print(a)
    print(type(a))
    # get_data1 = get_read(get_file_path('scripts_data','scripts_data_mail_pwd_login.yaml'))
    # print(get_data1)
    # print(get_data1[0]["mail"])
    # print(type(page.loggin_input_password))