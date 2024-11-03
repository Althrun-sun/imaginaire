import torch

# Check if CUDA is available
cuda_available = torch.cuda.is_available()
print(f"CUDA Available: {cuda_available}")

if cuda_available:
    # Check GPU name
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")

    # Check cuDNN availability
    cudnn_available = torch.backends.cudnn.is_available()
    print(f"cuDNN Available: {cudnn_available}")

    # Optional: Check cuDNN version if available
    if cudnn_available:
        print(f"cuDNN Version: {torch.backends.cudnn.version()}")

else:
    print("CUDA is not available. Ensure you have the correct drivers installed.")
