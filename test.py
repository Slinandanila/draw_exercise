import matplotlib.pyplot as plt

def visualize_squares(squares):
    fig, ax = plt.subplots()

    # Iterate through the squares and add them to the chart
    for square in squares:
        ax.add_patch(square)

    # Axes and graph settings
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Saving an image
    plt.savefig('squares_visualization.png')

    # Display graph
    plt.show()

# Usage example
square1 = plt.Rectangle((1, 1), 2, 2, color='blue')
square2 = plt.Rectangle((4, 4), 3, 3, color='red')

squares_to_visualize = [square1, square2]

visualize_squares(squares_to_visualize)
