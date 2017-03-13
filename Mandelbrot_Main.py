# Python code to compute, print and ave a png file of madnelbrot set at specified points
# num_grid_pts defines how large array.  Sticking with uniform grid but if variable scaling is desired split into
# num_grid_pts_x & num_grid_pts_y
# The tolerance is the number of times a specific point will be interated on to determine if it is in the set.
# x_min, x_max, y_min, y_max are boundary of calculation (-2,2,-2,2 encompass the set).
# Worth noting that functions use local variables and global variables carry "global tag"
import numpy as np
import matplotlib.pyplot as plt


# Plotting function creates a heatmap - Relied on by main.
def _plotting(values, tolerance, x_min, x_max, y_min, y_max):
	plt.xlabel("Real Axis")
	plt.ylabel("Imaginary Axis")
	plt.title("The Mandelbrot Set. Tolerance: %s" % tolerance)
	plt.grid(True)
	plt.imshow(values, origin="0,0", interpolation="none", extent=[x_min, x_max, y_min, y_max])
	plt.savefig("MandelBrot.png", bbox_inches="tight")
	plt.show()


# Algorithm to compute if point is within set - Relied on by main
def _mandel_calc(point, tolerance):
	z = 0
	for i in range(1, tolerance):
		if abs(z) > 2:
			return i
		z = z*z + point
	return 0


# Main function intialises & creates grid.  Dependent on _mandel_calc & _plotting.
def _mandelbrot_main(x_min, x_max, y_min, y_max, num_grid_pts, tolerance):
	real = np.linspace(x_min, x_max, num_grid_pts)
	imag = np.linspace(y_min, y_max, num_grid_pts)
	values = np.empty((num_grid_pts, num_grid_pts))
	for i in range(num_grid_pts):
		for j in range(num_grid_pts):
			values[j, i] = _mandel_calc(real[i] + 1j*imag[j], tolerance)
	_plotting(values, tolerance, x_min, x_max, y_min, y_max)
	return real

print("This code will compute the mandelbrot set for a user defined number of points between uer defined boundaries.\n")
print("The tolerance is the number of times a specific point will be interated on to determine if it is in the set.\n")
print("A plot is saved to file and then printed to screen.\n")
print("Note that -2 -> x -> 2 & -2 -> y -> 2 encompass the set.\n")

# Sample grids to run.
# _mandelbrot_main(-2, 2, -2, 2, 1000, 100)
# _mandelbrot_main(0, .5, .5, 1.0, 1000, 100)
# _mandelbrot_main(.5, .6, .3, .4, 1000, 100)
# _mandelbrot_main(.34, .36, .50, 5.2, 1000, 100
# _mandelbrot_main(.30, .32, .56, .58, 1000, 100)
# _mandelbrot_main(.36, .38, .58, .60, 1000, 50)

G_x_min = float(input("Input x_min:"))
G_x_max = float(input("Input x_max:"))
G_y_min = float(input("Input y_min:"))
G_y_max = float(input("Input y_max:"))
G_num_grid_pts = int(input("Input num_grid_pts:"))
G_tolerance = int(input("Input tolerance:"))

print("Inputs ok. Computing set ...")
_mandelbrot_main(G_x_min, G_x_max, G_y_min, G_y_max, G_num_grid_pts, G_tolerance)
