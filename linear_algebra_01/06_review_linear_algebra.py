import numpy as np
import torch
x = np.array([25, 2, 5])
print(x)

x_t = x.T
print(x_t)

x_p = torch.tensor([25, 2, 5])
print(x_p)

x_p_t = x_p.T
print(x_p_t)
