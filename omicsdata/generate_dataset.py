# -*- coding: utf-8 -*-

"""
@Time : 2023/6/21 16:28
@Author : Xiao Chen
@File : generate_dataset.py
"""

import pandas as pd
import scipy.io as sio
import yaml
import os


def save_mat_file(file_name, data):
    sio.savemat(file_name, {'data': data})


def process_one_row(csv_iter):
    data = csv_iter.to_numpy()
    sample_name = csv_iter.index
    return data, sample_name.values[0]


def generate_dataset(data_path, save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    data = pd.read_csv(data_path, index_col=0, iterator=True, chunksize=1)
    for dt in data:
        numer, sample_name = process_one_row(dt)
        path = os.path.join(save_path, sample_name + ".mat")
        save_mat_file(path, numer)


if __name__ == "__main__":
    print("="*30, " Test ", "="*30)
    # read arguments
    with open("generate_dataset.yml", 'r', encoding='utf-8') as f:
        args = yaml.load(f, Loader=yaml.FullLoader)
    print("Arguments: \n\t", args)
    generate_dataset(args['dna_data_path'], args['dna_save_path'])
    generate_dataset(args['rna_data_path'], args['rna_save_path'])
    generate_dataset(args['mirna_data_path'], args['mirna_save_path'])

