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

    def set_dataroot(self, path="/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets"):
        """
        Set the root directory of the data set, in order to facilitate the loading of data sets outside the project
        :param path: the absolute path of dataset
        :return: none
        """
        self._data_root_dir = path
        print("current dataset root is: ", path)

    def add_data_path(self, name):
        """
        add new dataset to framework
        :param name: dataset name
        :return: none
        """
        new_dir = os.path.join(self.data_root, "Other/" + name)
        if os.path.exists(new_dir):
            self.data_dir[name] = new_dir
            print("dataset dictionary is existed.")
        else:
            os.makedirs(new_dir)
            self.data_dir[name] = new_dir
            print("new dataset dictionary is created.")

    def get_data_path(self, name):
        return os.path.join(self._data_root_dir, self.data_dir[name])
