"""Mandlebrot class used to calculate the mandelbrot set."""
from datetime import datetime
from os import getenv
from pathlib import Path

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from numpy import empty, linspace


class Mandelbrot:
    """Mandelbrot."""

    def __init__(self):
        """Load config from Environment."""
        load_dotenv()
        self.tolerance = int(getenv("TOLERANCE", 75))
        self.grid_points = int(getenv("GRID_POINTS", 1000))
        self.x_min = float(getenv("X_MIN", -2))
        self.x_max = float(getenv("X_MAX", 2))
        self.y_min = float(getenv("Y_MIN", -2))
        self.y_max = float(getenv("Y_MAX", 2))

    def run(self):
        """Iterate through all grid points."""
        print("Computing set")
        # TODO: Refactor inefficient garbage.
        real = linspace(self.x_min, self.x_max, self.grid_points)
        imaginary = linspace(self.y_min, self.y_max, self.grid_points)
        values = empty((self.grid_points, self.grid_points))
        for i in range(self.grid_points):
            for j in range(self.grid_points):
                values[j, i] = self._mandel_calc(real[i] + 1j * imaginary[j])
        self._plotting(values)

    def _mandel_calc(self, point: int) -> int:
        """Check if a point remains in the mandelbrot set up to a certain tolerance."""
        z = 0
        for i in range(1, self.tolerance):
            if abs(z) > 2:
                return i
            z = z * z + point
        return 0

    def _plotting(self, values):
        """Create a heatmap of points."""
        date_time = datetime.now().isoformat()[:16]
        file_path = (
            Path(__file__).parent.parent / f"images/mandelbrot-{self.grid_points}-{self.tolerance}-{date_time}.png"
        )

        print("Plotting the set...")
        plt.xlabel("Real Axis")
        plt.ylabel("Imaginary Axis")
        plt.title("The Mandlebrot Set. Tolerance: %s" % self.tolerance)
        plt.grid(True)
        plt.imshow(values, interpolation="none", extent=[self.x_min, self.x_max, self.y_min, self.y_max])
        plt.savefig(file_path, bbox_inches="tight")
        plt.show()
