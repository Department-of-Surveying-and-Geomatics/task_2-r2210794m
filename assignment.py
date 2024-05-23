import csv
import matplotlib.pyplot as plt
from random import random


class Point:
    """
    This class represents a simple point in 2D space with x and y coordinates.

    Attributes:
        x (float): X-coordinate of the point.
        y (float): Y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initializes a Point object with its x and y coordinates.

        Args:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def get_x(self):
        """
        Returns the x-coordinate of the point.

        Returns:
            float: The x-coordinate of the point.
        """
        return self.x

    def get_y(self):
        """
        Returns the y-coordinate of the point.

        Returns:
            float: The y-coordinate of the point.
        """
        return self.y

    def translate(self, dx, dy):
        """
        Moves (translates) the point by the specified offsets.

        This method modifies the point's coordinates in-place.

        Args:
            dx (float): X-axis offset.
            dy (float): Y-axis offset.
        """
        self.x += dx
        self.y += dy

    def __str__(self):
        """
        Returns a string representation of the point in the format "(x, y)".

        Returns:
            str: String representation of the point.
        """
        return f"({self.x}, {self.y})"


def main():
    """
    Driver program to import point coordinates, plot them, translate them,
    and replot them in a different color.
    """

    # Read data from text file with more informative variable name and error handling
    filename = "data.txt"  # Replace with your actual file path
    try:
        points = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=" ")  # Use space delimiter
            for row in reader:
                points.append(Point(float(row[0]), float(row[1])))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Create plot
    fig, ax = plt.subplots()
    x, y = zip(*[(point.get_x(), point.get_y()) for point in points])
    plt.scatter(x, y)
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.title("Point Plot")
    plt.grid(True)

    # Move points by random offsets (clearer comments and avoid negative offsets)
    for point in points:
        point.translate(random() * 0.1, random() * 0.1)  # Random offset between 0 and 0.1

    # Replot points in red using the updated coordinates
    x, y = zip(*[(point.get_x(), point.get_y()) for point in points])
    plt.scatter(x, y, color='red', label="Translated Points")  # Add label for clarity

    # Enhance plot with informative legend
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
