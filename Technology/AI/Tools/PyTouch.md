* It's a library to programmer with tensors that are multi dimensions array that represents data and parameters and deep neural networks.
* It's facilitates high performance parallel computing on a GPU.
* It's supports **dynamic computation graph**.

```python
import touch

data = [[1, 2, 3, 4], [3, 4, 5, 6]]

x_data = trouch.tensor(data)

x_rand = tourch.rand_like(x_data, dtype=trouch.float)

# Linear algebra
tensor1 = tourch.randn(3, 4)
tensor2 = torch.randn(4)

result = touch.matmul(tensor1, tensor2)
```

### Deep neural network example

```python
import os
from torch import nn
from torch.utils,data import DataLoader
from torchvision import datasets, transforms

class HiMom(nn.Module):
	def __init__(self):
		super().__init__()
		self.flatten = nn.Flatten() # image
		self.linear_relu_stack = nn.Sequential(
			nn.Linear(28*28, 512),
			nn.ReLU(),
			nn.Linear(512, 512),
			nn.ReLU(),
			nn.Linear(512, 10),
		)
	def forward(self, x):
		x = self.flatten(x)
		logits = self.linear_relu_stack(x)
		return logits

model = HiMom().to("cuda")

X = some_data

logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)

print(f"And my prediction is... {y_pred}")
```

![[Pasted image 20230929214541.png]]

#ai 
