from PIL import Image
import numpy as np

# Assuming processor is already defined and provides the mean and std
image_mean = processor.image_processor.image_mean
image_std = processor.image_processor.image_std

batch_idx = 1  # Change to your desired index

# Get the pixel values for the specific image in the batch
pixel_values = batch["pixel_values"][batch_idx].numpy()

# Unnormalize the image
unnormalized_image = (pixel_values * np.array(image_std)[:, None, None]) + np.array(image_mean)[:, None, None]

# Clip the values to ensure they are in the correct range
unnormalized_image = np.clip(unnormalized_image, 0, 1)

# Scale to [0, 255] and convert to uint8
unnormalized_image = (unnormalized_image * 255).astype(np.uint8)

# Change the channel order from (C, H, W) to (H, W, C)
unnormalized_image = np.moveaxis(unnormalized_image, 0, -1)

# Create a PIL image and show it
image = Image.fromarray(unnormalized_image)
image.show()

