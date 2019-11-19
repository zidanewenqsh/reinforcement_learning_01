
import torch
import torch.nn as nn

class ExampleNet(nn.Module):

	def __init__(self):
		super(ExampleNet, self).__init__()
		self.conv2d_3 = nn.Conv2d(in_channels = 4, out_channels = 32, kernel_size = 8, stride = 4,  dilation = 1, groups = 1, bias = True)
		self.reLU_10 = nn.ReLU(inplace = False)
		self.conv2d_4 = nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 4, stride = 2,  dilation = 1, groups = 1, bias = True)
		self.reLU_11 = nn.ReLU(inplace = False)
		self.conv2d_5 = nn.Conv2d(in_channels = 64, out_channels = 64, kernel_size = 3, stride = 1,  dilation = 1, groups = 1, bias = True)
		self.reLU_8 = nn.ReLU(inplace = False)
		self.linear_7 = nn.Linear(in_features = 7*7*64, out_features = 512, bias = True)
		self.reLU_9 = nn.ReLU(inplace = False)
		self.linear_6 = nn.Linear(in_features = 512, out_features = 2, bias = True)

	def forward(self, x_para_1):
		print("x_para_1",x_para_1.shape)
		x_conv2d_3 = self.conv2d_3(x_para_1)
		print("x_conv2d_3",x_conv2d_3.shape)
		x_reLU_10 = self.reLU_10(x_conv2d_3)
		print("x_reLU_10",x_reLU_10.shape)
		x_conv2d_4 = self.conv2d_4(x_reLU_10)
		print("x_conv2d_4",x_conv2d_4.shape)
		x_reLU_11 = self.reLU_11(x_conv2d_4)
		print("x_reLU_11",x_reLU_11.shape)
		x_conv2d_5 = self.conv2d_5(x_reLU_11)
		print("x_conv2d_5",x_conv2d_5.shape)
		x_reLU_8 = self.reLU_8(x_conv2d_5)
		print("x_reLU_8",x_reLU_8.shape)
		x_reshape_12 = torch.reshape(x_reLU_8,shape = (-1,  7*7*64))
		print("x_reshape_12",x_reshape_12.shape)
		x_linear_7 = self.linear_7(x_reshape_12)
		print("x_linear_7",x_linear_7.shape)
		x_reLU_9 = self.reLU_9(x_linear_7)
		print("x_reLU_9",x_reLU_9.shape)
		x_linear_6 = self.linear_6(x_reLU_9)
		print("x_linear_6",x_linear_6.shape)
		return x_linear_6

if __name__ == '__main__':
	net = ExampleNet()
	a = torch.randn(5,4,84,84)
	b = net(a)
	print(b.shape)
