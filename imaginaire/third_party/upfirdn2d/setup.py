# Updated setup.py for upfirdn2d package
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
import torch

# Get CUDA version for compatibility checks
cuda_version = os.getenv('CUDA_VERSION')
torch_cuda_version = torch.version.cuda if torch.cuda.is_available() else 'None'
print('System CUDA Version:', cuda_version)
print('PyTorch CUDA Version:', torch_cuda_version)

# Set NVCC compilation arguments
nvcc_args = [
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_75,code=sm_75',
    '-Xcompiler', '-Wall', '-std=c++17',
    '-D__CUDA_NO_HALF_OPERATORS__',
    '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__'
]

setup(
    name='upfirdn2d_cuda',
    py_modules=['upfirdn2d'],
    ext_modules=[
        CUDAExtension(
            'upfirdn2d_cuda',
            ['./src/upfirdn2d_cuda.cc', './src/upfirdn2d_cuda_kernel.cu'],
            extra_compile_args={'cxx': ['-Wall', '-std=c++17'], 'nvcc': nvcc_args}
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)
