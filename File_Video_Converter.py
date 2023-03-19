import os
import struct
import numpy as np
from PIL import Image

# User input: path of the file to convert
input_file = input("Enter the path of the file to convert: ")

# Read binary data from file
with open(input_file, 'rb') as f:
    binary_data = f.read()

# Split binary data into chunks of 3 bytes
chunks = [binary_data[i:i+3] for i in range(0, len(binary_data), 3)]

# Define the size of each image in the sequence
image_size = (512, 512)

# Create an image sequence from the binary data
images = []
for chunk in chunks:
    # Pad the chunk with zeroes if its length is less than 3 bytes
    chunk += b'\x00' * (3 - len(chunk))
    # Convert the chunk to RGB values (0-255)
    r, g, b = struct.unpack('BBB', chunk)
    # Create an image with the RGB values
    img = Image.new('RGB', image_size, (r, g, b))
    # Add the image to the sequence
    images.append(img)

# Save the image sequence as PNG files
for i, img in enumerate(images):
    img.save(f'frame_{i:03d}.png')

print(f'Successfully converted {input_file} to an image sequence.')



#####  To convert the image sequence back to the original file, we can use a similar approach: ######



# User input: path of the directory containing the image sequence
input_dir = input("Enter the path of the directory containing the image sequence: ")

# Read the PNG files in the directory and extract their RGB values
images = []
for filename in sorted(os.listdir(input_dir)):
    if filename.endswith('.png'):
        img = Image.open(os.path.join(input_dir, filename))
        r, g, b = np.array(img).transpose((2, 0, 1))
        images.append((r, g, b))

# Merge the RGB values and save the binary data as a file
with open('restored_file', 'wb') as f:
    for r, g, b in images:
        f.write(bytes([r, g, b]))

print(f'Successfully restored the original file from the image sequence.')
