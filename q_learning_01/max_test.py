import torch

a = torch.randn(5,5)
b = torch.max(a[2])
print(a)
print(b)