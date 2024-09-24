import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from PIL import Image

# Get a batch of data from the DataLoader (assuming your dataloader yields a batch of images and labels)
data_iter = iter(dataloader)
images, labels = next(data_iter)

# Select the first image from the batch
image_tensor = images[0]

# Convert the tensor to a PIL image
# Assuming the image is normalized, we might need to denormalize it before displaying
# Assuming the image is [C, H, W] (Channel, Height, Width), we permute it to [H, W, C]
unloader = transforms.ToPILImage()
image = unloader(image_tensor)

# Display the image using matplotlib
plt.imshow(image)
plt.axis('off')  # Turn off the axis
plt.show()
