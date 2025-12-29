# Banana for scale

A Matplotlib colormap that uses banana colors.

```python
import numpy as np
import matplotlib.pyplot as plt
import banana_for_scale  # registers the colormap

x = np.linspace(0, 2 * np.pi, 200)
data = np.sin(x)[:, None] * np.cos(x)[None, :]

plt.imshow(data, cmap="banana")
plt.colorbar()
plt.show()
```
![Example plot using the banana-for-scale colormap](example.png)