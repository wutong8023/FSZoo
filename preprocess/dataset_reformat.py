"""
reformat dataset into：
- dataset name
    -- train
        ---class 0
        ---class 1
        ---class ..
    -- valid
        ---class 0
        ---class 1
        ---class ...
    -- test
        ---class 0
        ---class 1
        ---class ...
    class_file

Author: Tong
Time: 04-05-2020
"""
import os
import json
from utils import IOUtils

source_dic = "/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets/data_raw/supervisedRE/semeval"
target_dic = "/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets/data_filtered/supervisedRE/semeval"

IOUtils.check_path(target_dic)

files = {}
for f_path, dirs, fs in os.walk(source_dic):
    for f in fs:
        files[f.split(".")[0].split("_")[1]] = os.path.join(f_path, f)

with open(files["val"]) as val:
    rel_set = set()
    for line in val:
        data_point = json.loads(line)
        # dict_keys(['token', 'h', 't', 'relation'])
        rel_set.add(data_point["relation"])


def reformat_semeval(target_path, file_type="train"):
    data_dic = {}
    with open(files[file_type]) as in_file:
        for line in in_file:
            data_point = json.loads(line)
            # dict_keys(['token', 'h', 't', 'relation'])
            _rel = data_point["relation"]
            data_point.pop("relation")
            print(data_point)
            if _rel in data_dic.keys():
                data_dic[_rel].append(data_point)
            else:
                data_dic[_rel] = [data_point]
    return data_dic


data_dic = reformat_semeval(source_dic)

relation2id_file = "/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets/data_filtered/supervisedRE/semeval/" \
                   "semeval_rel2id.json"

relation2id = {}
with open(relation2id_file) as in_file:
