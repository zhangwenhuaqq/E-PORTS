import os

def get_file_path(config,config_base_path):
    base_path = os.path.dirname(os.path.dirname(__file__))
    #print(base_path)
    filepath = os.path.join(base_path,config,config_base_path)
    return filepath

if __name__=='__main__':
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(dir_path)
    get_data = (get_file_path('image', 'image2023_12_2913_28_S.png'))

    print(get_data)