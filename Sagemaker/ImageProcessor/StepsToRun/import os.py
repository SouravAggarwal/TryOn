import os
import torch

# Set environment variables
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:256'

# Clear CUDA memory cache
torch.cuda.empty_cache()