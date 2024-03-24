import torch

a = [[1.,2],[3,4]]

print(a)

print(torch.tensor(a))

print(torch.Tensor(2,3))

# 0, 2, 4, 6, 8
print(torch.arange(0, 10, 2))

print(torch.linspace(0, 10, 5))

print(torch.randn(2, 3))

print(torch.ones(2, 3))

print(torch.zeros(2, 3))

print(torch.full((2, 4), 30))

a = torch.tensor(a)
print(a.dtype)

a = a.type(torch.DoubleTensor)
print(a.dtype)

a = a.double()
print(a.dtype)