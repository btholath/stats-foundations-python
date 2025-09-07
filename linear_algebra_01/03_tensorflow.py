"""
Scalars in TensorFlow (version 2.0 or later)
Tensors created with a wrapper, all of which you can read about here:https://www.tensorflow.org/guide/tensor

tf.Variable
tf.constant
tf.placeholder
tf.SparseTensor
Most widely-used is tf.Variable, which we'll use here.

As with TF tensors, in PyTorch we can similarly perform operations, and we can easily convert to and from NumPy arrays.

Also, a full list of tensor data types is available
https://www.tensorflow.org/api_docs/python/tf/dtypes/DType
"""

import tensorflow as tf

# Create a 2D tensor (e.g., representing loan data features)
x_tf = tf.Variable([[1, 2], [3, 4]], dtype=tf.float32)
print("x_tf = ", x_tf)

# Perform a matrix operation (e.g., scaling, common in ML preprocessing)
scaled_x = tf.multiply(x_tf, 2.0)
print("Scaled x_tf = ", scaled_x)

