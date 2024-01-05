import os

def get_file_path(config,config_base_path):
    base_path = os.path.dirname(os.path.dirname(__file__))
    #print(base_path)
    filepath = os.path.join(base_path,config,config_base_path)
    return filepath



if __name__=='__main__':

    res = get_file_path('page_data','page_data_mail_pwd-login.yaml')
    print(res)