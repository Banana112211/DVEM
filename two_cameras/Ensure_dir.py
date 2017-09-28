
import os

def ensure_dir(file_path):
    """This function will create a new order if the order does'n exist"""
    try:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(file_path)
    except:
        print "folder already exist"        