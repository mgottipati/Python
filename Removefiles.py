import os
import shutil
import time
path = "/Users/ggottipati/Desktop/new/"
days = 2
seconds = time.time()-(days*24*3600)

def remove_folder(path):
    if not shutil.rmtree(path):
        print("folder remove successful")

def remove_file(path):
    if not os.remove(path):
        print("file remove successful")

def get_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if os.path.exists(path):
    for root_folder,folders,files in os.walk(path):
        if(seconds >= get_age(root_folder)):
            remove_folder(root_folder)
        for files in 
            remove_file 
            file_path = os.path.join(root_folder, file)

            
