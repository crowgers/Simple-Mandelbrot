"""Entry point for the app."""
from mandelbrot import Mandelbrot


def main():
    """Draw the mandlebrot set."""
    mandel = Mandelbrot()
    print(
        """
        This code will compute the mandelbrot set for a user defined number of points between uer defined boundaries.
        The tolerance is the number of times a specific point will be iterated on to determine if it is in the set.
        A plot is saved to file and then printed to screen.
        Note that -2 -> x -> 2 & -2 -> y -> 2 encompass the set.
    """
    )
    mandel.run()


if __name__ == "__main__":
    main()
