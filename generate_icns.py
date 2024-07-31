import os
from PIL import Image

icon_sizes = [16, 32, 128, 256, 512, 1024]
input_image = 'icon.png'
output_folder = 'IconSet.iconset'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for size in icon_sizes:
    img = Image.open(input_image)
    img = img.resize((size, size), Image.LANCZOS)
    img.save(os.path.join(output_folder, f'icon_{size}x{size}.png'))

# Create @2x images for Retina displays
for size in icon_sizes[:-1]:  # Skip 1024 size as it is already @2x for 512
    img = Image.open(input_image)
    img = img.resize((size * 2, size * 2), Image.LANCZOS)
    img.save(os.path.join(output_folder, f'icon_{size}x{size}@2x.png'))

