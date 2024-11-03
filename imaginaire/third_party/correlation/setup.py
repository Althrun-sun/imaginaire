import os
import torch
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
from setuptools import setup
import subprocess

# Determine CUDA version
cuda_version = torch.version.cuda
print(f"Detected PyTorch CUDA version: {cuda_version}")
system_cuda_version = os.getenv('CUDA_VERSION', 'Unknown')
print(f"Detected system CUDA version: {system_cuda_version}")

# Define NVCC arguments
nvcc_args = [
    '-D__CUDA_NO_HALF_OPERATORS__',
    '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__',
    '-Xcompiler',
    '-fPIC',
    '-std=c++17'  # Updated for C++17 support
]

# Add architecture flags for 4060 Ti (Ada Lovelace, usually compute_89)
nvcc_args.extend(['-gencode', 'arch=compute_89,code=sm_89'])
print(f"Using NVCC compilation arguments: {nvcc_args}")

# Check environment and versions
print("PyTorch and CUDA configuration:")
print(f"  PyTorch version: {torch.__version__}")
print(f"  CUDA available: {torch.cuda.is_available()}")
print(f"  PyTorch CUDA Version: {torch.version.cuda}")
print(f"  System CUDA Version: {system_cuda_version}")

# Proceed with setup
setup(
    name='correlation_cuda',
    ext_modules=[
        CUDAExtension(
            name='correlation_cuda',
            sources=['src/correlation_cuda.cc', 'src/correlation_cuda_kernel.cu'],
            extra_compile_args={
                'cxx': ['-O3'],
                'nvcc': nvcc_args
            }
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
print("Setup script executed successfully.")
