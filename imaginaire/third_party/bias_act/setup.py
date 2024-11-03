# flake8: noqa
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
import torch

# Detect PyTorch CUDA version
torch_cuda_version = torch.version.cuda
print('Torch CUDA Version:', torch_cuda_version)

# Detect system CUDA version
cuda_version = os.getenv('CUDA_VERSION')
print('System CUDA Version:', cuda_version)

nvcc_args = list()
nvcc_args.append('-gencode')
nvcc_args.append('arch=compute_70,code=sm_70')
nvcc_args.append('-gencode')
nvcc_args.append('arch=compute_75,code=sm_75')
nvcc_args.append('-gencode')
nvcc_args.append('arch=compute_80,code=sm_80')
nvcc_args.append('-gencode')
nvcc_args.append('arch=compute_89,code=sm_89')  # Updated for Ada Lovelace architecture

# Add additional arguments to handle compatibility with PyTorch and CUDA versions
nvcc_args += [
    '-Xcompiler', '-Wall', '-std=c++17',
    '-D__CUDA_NO_HALF_OPERATORS__',
    '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_BFLOAT16_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__',
    '--expt-relaxed-constexpr'
]

print("Using NVCC compilation arguments:", nvcc_args)

setup(
    name='bias_act_cuda',
    py_modules=['bias_act'],
    ext_modules=[
        CUDAExtension('bias_act_cuda', [
            './src/bias_act_cuda.cc',
            './src/bias_act_cuda_kernel.cu'
        ], extra_compile_args={
            'cxx': ['-Wall', '-std=c++17'],
            'nvcc': nvcc_args
        })
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
