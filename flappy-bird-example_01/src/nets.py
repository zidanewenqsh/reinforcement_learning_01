import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv_84_7 = nn.Sequential(
            nn.Conv2d(4, 32, 8, 4),
            nn.ReLU(),
            nn.Conv2d(32, 64, 4, 2),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, 1),
            nn.ReLU()
        )
        self.linear_1 = nn.Sequential(
            nn.Linear(64 * 7 * 7, 512),
            nn.ReLU(),
            nn.Linear(512, 2)
        )

    def forward(self, input:torch.Tensor) -> torch.Tensor:
        y = self.conv_84_7(input)
        y = y.reshape(-1,64 * 7 * 7)
        output = self.linear_1(y)
        return output

if __name__ == '__main__':
    net = Net()
    a = torch.randn(5, 4, 84, 84)
    b = net(a)
    print(b.shape)