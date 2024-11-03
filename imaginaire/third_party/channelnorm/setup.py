# flake8: noqa
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os

# Detect CUDA version
cuda_version = os.getenv('CUDA_VERSION')
print(f'Detected CUDA version: {cuda_version}')

# Define NVCC arguments based on CUDA version
nvcc_args = [
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_75,code=sm_75',
    '-Xcompiler', '-Wall', '-std=c++17'  # Updated to C++17
]

# Add newer architecture compatibility if CUDA version >= 11
if cuda_version is not None and cuda_version >= '11.0':
    nvcc_args.extend(['-gencode', 'arch=compute_80,code=sm_80'])

# Include additional compute compatibility for CUDA >= 12.0
if cuda_version is not None and cuda_version >= '12.0':
    nvcc_args.extend(['-gencode', 'arch=compute_89,code=sm_89'])

# Display final NVCC arguments for debugging
print(f'Using NVCC compilation arguments: {nvcc_args}')

setup(
    name='channelnorm_cuda',
    py_modules=['channelnorm'],
    ext_modules=[
        CUDAExtension('channelnorm_cuda', [
            './src/channelnorm_cuda.cc',
            './src/channelnorm_cuda_kernel.cu'
        ], extra_compile_args={'cxx': ['-Wall', '-std=c++17'], 'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
print("Setup script executed successfully for channelnorm.")
