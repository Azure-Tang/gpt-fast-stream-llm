import torch
import os
def save_kv_to_file(k_tensor, v_tensor, path, file_path_k, file_path_v):
    """
    保存键k和值v向量到指定的文件中。
    
    参数：
    - k_tensor: 要保存的键k的Tensor。
    - v_tensor: 要保存的值v的Tensor。
    - file_path_k: 保存键k向量的文件路径。
    - file_path_v: 保存值v向量的文件路径。
    """
    if not os.path.exists(path):
        os.makedirs(path)
    file_path_k = path + file_path_k
    file_path_v = path + file_path_v
    torch.save(k_tensor, file_path_k)
    torch.save(v_tensor, file_path_v)

def save_block_to_file(block, file_path, name):
    """
    保存block到指定的文件中。
    
    参数：
    - block: 要保存的block。
    - file_path: 保存block的文件路径。
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path = file_path + name
    torch.save(block, file_path)

args = None