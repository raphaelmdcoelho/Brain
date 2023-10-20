Tensors are a specialized data structure that are very similar to arrays and matrices. In [[PyTorch]], we use tensors to encode the inputs and outputs of a model, as well as the mode's parameters.

Tensors are similar to [[NumPy]]'s ndarrays, except that tensors can run on GPUs or other hardware accelerators. In fact, tensors and NumPy arrays can often share the same underlying memory, eliminating the need to copy data. Tensors are also optimized for automatic differentiation.

Tensors extend the concepts of [[scalars]] (0D tensors), [[vectors]] (1D tensors), and [[matrices]] (2D tensors).

So Tensors are just a generic form for matrices.

```python
import torch
import numpy as np
```

### Initializing a Tensor

Tensors can be initialized in various ways. Take a look at the following examples:

**Directly from data**

Tensors can be created directly from data. The data type is automatically inferred.

```python
data = [[1,2],[3,4]]
x_data = torch.tensor(data)
```

**From a NumPy array**

Tensors can be created from NumPy arrays.

```python
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
```

**From another tensor**

The new tensor retains the properties (shape, datatype) of the argument tensor, unless explicitly overridden.

```python
x_ones = torch.ones_like(x_data)
printf(f"Ones Tensor: \n {x_ones} \n")

#Ones Tensor:
 #tensor([[1, 1],
		#[1, 1]])

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

#Random Tensor:
 #tensor([[0.4223, 0.1719],
        #[0.3184, 0.2631]])
```

**Attributes of a Tensor**

Tensor attributes describe their shape, datatype, and the device on which they are stored.

```python
tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
```

**Operations on Tensors**

Over 100 tensor operations, including arithmetic, linear algebra, matrix manipulation.

Each of these operations can be run on the GPU (at typically higher speeds than on a CPU). If you're using Colab, allocate a GPU by going to Runtime > Change runtime type > GPU.

By default, tensors are created on the CPU. We need to explicitly move tensors to the GPU using `.to` method (after checking for GPU availability). Keep in mind that copying large tensors across devices can be expensive in terms of time and memory.

```python
if torch.cuda.is_available():
	tensor - tensor.to('cuda')
```

* Joining tensors
* Arithmetic operations
* Single-element tensors
* In-place operations

### References

* [(46) Tensors for Neural Networks, Clearly Explained!!! - YouTube](https://www.youtube.com/watch?v=L35fFDpwIM4)


#ai 