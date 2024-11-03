import torch
import correlation_cuda

class CorrelationFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input1, input2, pad_size, kernel_size, max_displacement, stride1, stride2):
        print("Forward pass called with parameters:")
        print(f"  pad_size: {pad_size}, kernel_size: {kernel_size}")
        print(f"  max_displacement: {max_displacement}, stride1: {stride1}, stride2: {stride2}")
        
        # Save parameters and inputs for backward computation
        ctx.save_for_backward(input1, input2)
        ctx.pad_size = pad_size
        ctx.kernel_size = kernel_size
        ctx.max_displacement = max_displacement
        ctx.stride1 = stride1
        ctx.stride2 = stride2

        # Execute the CUDA forward function
        try:
            result = correlation_cuda.forward(input1, input2, pad_size, kernel_size, max_displacement, stride1, stride2)
            print("Forward pass completed successfully.")
            return result
        except Exception as e:
            print(f"Error during forward pass: {e}")
            raise

    @staticmethod
    def backward(ctx, grad_output):
        print("Backward pass initiated.")
        input1, input2 = ctx.saved_tensors
        try:
            grad_input1, grad_input2 = correlation_cuda.backward(
                input1, input2, grad_output,
                ctx.pad_size, ctx.kernel_size, ctx.max_displacement,
                ctx.stride1, ctx.stride2
            )
            print("Backward pass completed successfully.")
            return grad_input1, grad_input2, None, None, None, None, None
        except Exception as e:
            print(f"Error during backward pass: {e}")
            raise

class Correlation(torch.nn.Module):
    def __init__(self, pad_size, kernel_size, max_displacement, stride1, stride2):
        super(Correlation, self).__init__()
        self.pad_size = pad_size
        self.kernel_size = kernel_size
        self.max_displacement = max_displacement
        self.stride1 = stride1
        self.stride2 = stride2
        print("Correlation Module initialized with:")
        print(f"  pad_size: {pad_size}, kernel_size: {kernel_size}")
        print(f"  max_displacement: {max_displacement}, stride1: {stride1}, stride2: {stride2}")

    def forward(self, input1, input2):
        print("Calling CorrelationFunction.forward()")
        return CorrelationFunction.apply(input1, input2, self.pad_size, self.kernel_size, self.max_displacement, self.stride1, self.stride2)
