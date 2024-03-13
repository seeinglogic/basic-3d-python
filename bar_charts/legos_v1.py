import matplotlib.pyplot as plt
import numpy as np


def plot_3d_bar_chart(rows_data, column_names, colors):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate grid for row and column positions
    _x = np.arange(len(column_names))
    _y = np.arange(len(rows_data))
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    
    # Flatten the Z values and calculate bottom
    top = np.array([value for values in rows_data.values() for value in values])
    bottom = np.zeros_like(top)
    width = 1
    depth = 0.5 # want room between rows
    
    # Plot bars
    for i in range(len(x)):
        row_index = int(y[i])
        color = colors[row_index]

        # Don't draw bars of zero height
        if top[i] == 0:
            continue

        ax.bar3d(x[i], y[i], bottom[i], width, depth, top[i], color=color, shade=True)

    # Set row and column labels
    ax.set_xticks(_x + width / 2)
    ax.set_xticklabels(column_names)
    ax.set_yticks(_y + depth / 2)
    ax.set_yticklabels(rows_data.keys())
    
    ax.set_title('LEGO Themes: From Generic to Franchise')
    plt.show()


column_names = [
    "'65-'69",
    "'70-'74",
    "'75-'79",
    "'80-'84",
    "'85-'89",
    "'90-'94",
    "'95-'99",
    "'00-'04",
    "'05-'09",
    "'10-'14",
    "'15-'17",
]
lego_colors = [
    'red',
    'pink',
    'orange',
    'blue',
    'goldenrod',
    'green',
    'purple',
    'cyan',
]

# inverted for aesthetics
lego_data_rows = {
    'Collectible Minifigures': [0, 0, 0, 0, 0, 0, 0, 0, 6, 287, 148],
    'Star Wars': [0, 0, 0, 0, 0, 0, 13, 120, 117, 195, 157],
    'Gear': [0, 0, 1, 1, 1, 0, 5, 22, 275, 62, 66],
    'Seasonal': [0, 0, 2, 0, 7, 6, 58, 176, 242, 402, 30],
    'Technic': [0, 0, 28, 22, 48, 80, 132, 91, 40, 56, 36],
    'Town': [0, 0, 53, 74, 116, 128, 208, 80, 164, 173, 102],
    'Service Packs': [0, 1, 45, 74, 167, 78, 82, 4, 0, 3, 0],
    'Universal Building Set': [4, 45, 29, 53, 106, 65, 124, 15, 0, 0, 0],
}
lego_colors = lego_colors[::-1]


plot_3d_bar_chart(lego_data_rows, column_names, lego_colors)
