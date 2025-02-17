"""
Preprocess today's MNIST dataset into 1989 version's size/format (approximately)
http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf

Some relevant notes for this part:
- 7291 digits are used for training
- 2007 digits are used for testing
- each image is 16x16 pixels grayscale (not binary)
- images are scaled to range [-1, 1]
- paper doesn't say exactly, but reading between the lines I assume label targets to be {-1, 1}
"""

import numpy as np
import torch
import torch.nn.functional as F
from torchvision import datasets

# -----------------------------------------------------------------------------

torch.manual_seed(1337)
np.random.seed(1337)

for split in {'train'}:

    data = datasets.MNIST('./data', train=split=='train', download=True)

    n = 1
    rp = np.random.permutation(len(data))[:n]

    X = torch.full((n, 1, 4, 4), 0.0, dtype=torch.float32)
    Y = torch.full((n, 10), -1.0, dtype=torch.float32)
    for i, ix in enumerate(rp):
        I, yint = data[int(ix)]
        print("# I: ", I)
        print("# yint: ", yint)
        # PIL image -> numpy -> torch tensor -> [-1, 1] fp32
        xi = torch.from_numpy(np.array(I, dtype=np.float32)) / 127.5 - 1.0
        print("# xi1: ", xi)
        # add a fake batch dimension and a channel dimension of 1 or F.interpolate won't be happy
        xi = xi[None, None, ...]
        # resize to (16, 16) images with bilinear interpolation
        xi = F.interpolate(xi, (4, 4), mode='bilinear')
        print("# xi2: ", xi)
        X[i] = xi[0] # store
        print("# X: ", X)
        # set the correct class to have target of +1.0
        Y[i, yint] = 1.0
        print("# Y: ", Y)

    # torch.save((X, Y), split + '1989.pt')

