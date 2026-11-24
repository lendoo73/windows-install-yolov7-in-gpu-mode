import torch

print("Torch:", torch.__version__)
print("CUDA:", torch.version.cuda)
print("cuDNN:", torch.backends.cudnn.version())

torch.backends.cudnn.enabled = False

x = torch.randn(1, 3, 640, 640, device="cuda")
conv = torch.nn.Conv2d(3, 32, 3, padding=1).cuda()

y = conv(x)

print(y.shape)
print("SUCCESS")