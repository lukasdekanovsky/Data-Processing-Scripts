import numpy as np
import matplotlib.pyplot as plt

# Read the pixel values from the .txt file
pixel_values = np.loadtxt('./data/2D_matice.txt')

# Create a figure and axis
fig, ax = plt.subplots()
# Display the pixel values as an image
img = ax.imshow(pixel_values, cmap='viridis')
# Add a colorbar for reference
cbar = fig.colorbar(img)

# Adjust the visual properties
ax.set_title('Pixel Values')
ax.set_xlabel('X')
ax.set_ylabel('Y')
cbar.set_label('Intensity')

# Show the plot
plt.show()