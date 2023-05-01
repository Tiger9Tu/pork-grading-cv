import torch
from torchvision import transforms
from PIL import Image
# Define the transform to be applied to the image
transform = transforms.Compose([
    transforms.ToTensor()
])

# Load the image
image = Image.open('data/pork.jpg')

# Apply the transform to the image
image_tensor = transform(image)

# Reshape the tensor to have 3 dimensions (channels, height, width)
image_tensor = image_tensor.unsqueeze(0)

# Split the image tensor into 9 equal parts
split_tensors = torch.split(image_tensor, 3)

# Print the shape of each split tensor
for tensor in split_tensors:
    print(tensor.shape)
