# --------------------------------------------------------
# Deformable Convolutional Networks
# Copyright (c) 2017 Microsoft
# Licensed under The Apache-2.0 License [see LICENSE for details]
# Written by Yuwen Xiong, Songyang Zhang
# --------------------------------------------------------
import os
import sys
# os.environ['PYTHONUNBUFFERED'] = '1'
# os.environ['MXNET_CUDNN_AUTOTUNE_DEFAULT'] = '0'
# os.environ['MXNET_ENABLE_GPU_P2P'] = '0'
this_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(this_dir, '..', '..', 'dff_rfcn'))
sys.path.insert(0, '/home/syzhang/mxnet_dff/python')
import train_end2end_tb

if __name__ == "__main__":
    train_end2end_tb.main()
