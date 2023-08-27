import matplotlib.pyplot as plt

# Example data1 and data2 as lists of lists (with 0s and 1s)
data1 = [[1, 1, 1],
         [0, 0, 1],
         [0, 0, 1]]

data2 = [[0.2, 0.4, 0.6],
         [0.8, 1.0, 0.2],
         [0.4, 0.6, 0.8]]

# Calculate the number of rows (or columns) and the cell size based on data1's dimensions
num_cells = len(data1)  # Since rows and columns are the same
cell_size = 10 / num_cells

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the background heatmap (map1) with grid-like appearance
cax1 = ax.imshow(data1, cmap='hot', interpolation='nearest', extent=[0, 10, 0, 10], vmin=0, vmax=1)

# Add grid lines to the background heatmap
for y in range(num_cells + 1):
    plt.axhline(y * cell_size, color='black', linewidth=1)
for x in range(num_cells + 1):
    plt.axvline(x * cell_size, color='black', linewidth=1)

# Overlay the second heatmap (map2) as squares based on values
for y in range(num_cells):
    for x in range(num_cells):
        value = data2[num_cells - 1 - y][x]  # Corrected mapping here
        if value > 0:
            square = plt.Rectangle((x * cell_size, y * cell_size), cell_size * value, cell_size * value,
                                   color='blue', alpha=0.5)
            ax.add_patch(square)

# Set aspect ratio to be equal, so cells are squares
ax.set_aspect('equal')

# Add a colorbar for map1
cbar1 = plt.colorbar(cax1, ax=ax)
cbar1.set_label('Data 1')

plt.title('Combined Heatmaps')

plt.show()
