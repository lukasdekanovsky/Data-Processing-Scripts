import numpy as np
import matplotlib as mpl
import imageio
import matplotlib.pyplot as plt

# 1) Define the file path
file_path_source = "./data/scanning_for_gif"
file_path_result = "./vystupy/scan_gif_test"

# 2) Read the pixel values from the .TXTs file and save .PNGs
for step in range(27):
    pixel_values = np.loadtxt(f'{file_path_source}/en_05_smooth_pos__{step}.txt')
    print(step)

    # individual PNG creation for each step
    fig, ax = plt.subplots()
    img = ax.imshow(pixel_values, cmap='viridis')
    cbar = fig.colorbar(img)

    # Adjust the visual properties
    ax.set_title('Scan for 5keV')
    ax.set_xlabel('pixels (0-256)')
    ax.set_ylabel('pixels (0-256)')
    cbar.set_label('Intensity')

    # Save the plot as a PNG file
    plt.savefig(f'{file_path_result}/raw_{step}.png')
    plt.close()
print(".PNGs generated successfully!")

# 3) GIF generation from the individual .PNGs
# Get the list of PNG files by comprehension
png_files = [f'{file_path_result}/raw_{step}.png' for step in range(27)]
print(png_files)
# Create the GIF file path
gif_file_path = f'{file_path_result}/scan_gif.gif'
# Set the frame rate (in seconds per frame)
frame_rate = 1

# Create the GIF from the PNG files
with imageio.get_writer(gif_file_path, mode='I', duration=frame_rate) as writer:
    for png_file in png_files:
        image = imageio.imread(png_file)
        writer.append_data(image)
print("GIF created successfully!")
