# flake8: noqa
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
import torch

# Detect CUDA version
cuda_version = torch.version.cuda
system_cuda_version = os.getenv('CUDA_VERSION')

print(f"PyTorch CUDA version: {cuda_version}")
print(f"System CUDA version: {system_cuda_version}")

# NVCC arguments
nvcc_args = [
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_75,code=sm_75',
    '-gencode', 'arch=compute_89,code=sm_89',  # For Ada Lovelace
    '-Xcompiler', '-Wall',
    '-std=c++17',
    '-D__CUDA_NO_HALF_OPERATORS__', '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__'
]

print("Using NVCC compilation arguments:", nvcc_args)

setup(
    name='resample2d_cuda',
    py_modules=['resample2d'],
    ext_modules=[
        CUDAExtension('resample2d_cuda', [
            './src/resample2d_cuda.cc',
            './src/resample2d_kernel.cu'
        ], extra_compile_args={
            'cxx': ['-Wall', '-std=c++17'],
            'nvcc': nvcc_args
        })
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
