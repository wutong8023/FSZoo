"""
path of resources

Author: Tong
Time: 25-04-2020
"""

import os
import json

class Config():
    def __init__(self):
        # absolute path
        _data_root_dir = "/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets"
        data_dir = {
            "semeval": "data_filtered/supervisedRE/semeval"
        }


    @classmethod
    def set_dataroot(cls, path="/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets"):
        """
        Set the root directory of the data set, in order to facilitate the loading of data sets outside the project
        :param path: the absolute path of dataset
        :return: none
        """
        cls._data_root_dir = path
        print("current dataset root is: ", path)

    @classmethod
    def add_data_path(cls, name):
        """
        add new dataset to framework
        :param name: dataset name
        :return: none
        """
        new_dir = os.path.join(cls.data_root, "Other/"+name)
        if os.path.exists(new_dir):
            cls.data_dir[name] = new_dir
            print("dataset dictionary is existed.")
        else:
            os.makedirs(new_dir)
            cls.data_dir[name] = new_dir
            print("new dataset dictionary is created.")

    @classmethod
    def get_data_path(cls, name):
        return os.path.join(cls._data_root_dir, cls.data_dir[name])


    
    








