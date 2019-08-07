import torch
import numpy as np
import torch.nn as nn
import pickle
import torch.nn.functional as F


class OneLayerNet(nn.Module):

    def __init__(self):
        super(OneLayerNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 2, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(2, 3, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(3, 1, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        return x


num_epochs = 6

pickle_off = open("Data.pickle", "rb")
train = pickle.load(pickle_off)

model = OneLayerNet().double()

# criterion and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(num_epochs):
    for i, (image, move) in enumerate(train):
        # Run the forward pass
        if i >= 100:
            image = torch.from_numpy(image).double().unsqueeze(dim=0).unsqueeze(dim=0)
            move = torch.from_numpy(move).double()
            output = model(image).squeeze()
            loss = criterion(output, move)
            print(loss)
            # Backprop and perform Adam optimisation
            optimizer.zero_grad()
            loss.squeeze().backward()
            optimizer.step()
params = list(model.parameters())
print(params)
# test
print('\n\n\n')
for i, (image, move) in enumerate(train):
    # Run the forward pass
    if i < 100:
        image = image.astype(dtype=np.float32)
        move = move.astype(dtype=np.float32)
        image = torch.from_numpy(image).double().unsqueeze(dim=0).unsqueeze(dim=0)
        move = torch.from_numpy(move).double()
        output = model(image).squeeze()
        output[output >= 0.5] = 1
        output[output < 0.5] = 0
        loss = criterion(output, move)
        print(loss)
