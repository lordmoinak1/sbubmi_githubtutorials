import numpy as np

def test_function(a, b):
  x = np.random.randn(a, b)
  return x

if __name__ == "__main__":
  a = 3
  b = 4
  x = test_functional(a, b)
  
  print(x)
