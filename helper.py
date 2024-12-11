import os
import sys

def get_file_name(test=True):

    file_name = sys.argv[0]
    base_path = os.path.dirname(file_name)
    file_name = os.path.basename(file_name).split('.')[0] + '.txt'
    data_dir = '/datas/'
    if test:
        return base_path+data_dir+"test.txt"
    
    return base_path + data_dir + file_name

    

print(get_file_name(False))
